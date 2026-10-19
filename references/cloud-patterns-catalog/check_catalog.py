#!/usr/bin/env python3
"""Check this catalog's deliberately simple inline Markdown links and inventory.

Run from any directory. --complete also rejects unfinished inventory entries.
External URLs are not fetched. --self-test exercises failures in temporary copies.
"""
import argparse
import json
import re
import shutil
import sys
import tempfile
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
ASPECTS = {'context', 'problem', 'forces', 'solution', 'sketch', 'results',
           'consequences', 'related-patterns', 'examples'}


def anchors(text):
    counts = Counter()
    result = set()
    for heading in re.findall(r'^#{1,6}\s+(.+)', text, re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        result.add(slug + (f'-{counts[slug]}' if counts[slug] else ''))
        counts[slug] += 1
    return result


def check(root, complete=False):
    errors = []
    def fail(path, reason):
        errors.append(f'{path}: {reason}')
    try:
        rows = json.loads((root / 'inventory.json').read_text())
    except (OSError, ValueError) as exc:
        return [f'inventory.json: {exc}']
    for key in ('name', 'slug'):
        for value, count in Counter(row[key] for row in rows).items():
            if count > 1:
                fail('inventory.json', f'duplicate {key}: {value}')
    texts = {p.resolve(): p.read_text() for p in root.rglob('*.md')}
    graph = {p: set() for p in texts}
    for path, text in texts.items():
        rel = path.relative_to(root)
        for target in LINK.findall(text):
            target = target.strip().strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if resolved.is_dir():
                resolved = resolved / 'README.md'
            if not resolved.is_relative_to(root):
                fail(rel, f'link escapes catalog: {target}')
            elif not resolved.exists():
                fail(rel, f'broken link: {target}')
            elif parsed.fragment and resolved.suffix == '.md' and unquote(parsed.fragment) not in anchors(texts.get(resolved, '')):
                fail(rel, f'missing anchor: {target}')
            if resolved in texts:
                graph[path].add(resolved)
    visited = set()
    todo = [(root / 'README.md').resolve()]
    while todo:
        path = todo.pop()
        if path not in visited:
            visited.add(path)
            todo.extend(graph.get(path, ()))
    for path in texts.keys() - visited:
        fail(path.relative_to(root), 'unreachable from README.md')
    index = texts.get(root / 'INDEX.md', '')
    expected_folders = set()
    identities = []
    for row in rows:
        slug = row['slug']
        folder = root / 'patterns' / slug
        landing = folder / 'README.md'
        if row['status'] != 'complete':
            if complete:
                fail('inventory.json', f'incomplete pattern: {row["name"]}')
            if folder.exists():
                fail(folder.relative_to(root), 'folder exists for unfinished inventory entry')
            continue
        expected_folders.add(slug)
        text = texts.get(landing, '')
        identity = f'<!-- pattern: {slug} -->'
        if identity not in text or not text.startswith(f'# {row["name"]}\n'):
            fail(landing.relative_to(root), 'missing canonical identity or title')
        entry = f'[{row["name"]}](patterns/{slug}/README.md)'
        if index.count(entry) != 1:
            fail('INDEX.md', f'expected exactly one entry for {slug}')
        if '(../../INDEX.md)' not in text:
            fail(landing.relative_to(root), 'missing index backlink')
        supported = set(row.get('aspects', []))
        unavailable = row.get('unavailable', {})
        if supported | set(unavailable) != ASPECTS or supported & set(unavailable):
            fail('inventory.json', f'{slug}: aspects must be available or explicitly unavailable')
        for aspect, reason in unavailable.items():
            if not reason or f'**{aspect}:** {reason}' not in text:
                fail(landing.relative_to(root), f'unexplained unavailable aspect: {aspect}')
        actual = {p.stem for p in folder.glob('*.md') if p.name != 'README.md'}
        if actual != supported:
            fail(folder.relative_to(root), f'aspect files disagree with inventory: {sorted(actual ^ supported)}')
        for aspect in supported:
            page = folder / f'{aspect}.md'
            body = texts.get(page, '')
            if f'({aspect}.md)' not in text:
                fail(landing.relative_to(root), f'missing aspect link: {aspect}')
            if '(README.md)' not in body:
                fail(page.relative_to(root), 'missing landing backlink')
            if not body.startswith(f'# {row["name"]} — '):
                fail(page.relative_to(root), 'missing pattern identification')
            if not re.search(r'^Source: .*\[.+?\]\(.+?\)', body, re.M):
                fail(page.relative_to(root), 'missing source reference')
            paragraphs = [p for p in body.split('\n\n') if p and not p.startswith(('#', 'Source:', '[Back'))]
            if not paragraphs:
                fail(page.relative_to(root), 'empty aspect body')
    folders = {p.name for p in (root / 'patterns').iterdir() if p.is_dir()} if (root / 'patterns').exists() else set()
    if folders != expected_folders:
        fail('patterns/', f'folders disagree with inventory: {sorted(folders ^ expected_folders)}')
    for landing in (root / 'patterns').glob('*/README.md'):
        identities.extend(re.findall(r'<!-- pattern: (.*?) -->', landing.read_text()))
    for identity, count in Counter(identities).items():
        if count > 1:
            fail('patterns/', f'duplicate canonical identity: {identity}')
    indexed = set(re.findall(r'\]\(patterns/([^/]+)/README.md\)', index))
    if indexed != expected_folders:
        fail('INDEX.md', f'index disagrees with inventory: {sorted(indexed ^ expected_folders)}')
    return errors


def self_test(root):
    assert not check(root), check(root)
    rows = json.loads((root / 'inventory.json').read_text())
    slug = next(row['slug'] for row in rows if row['status'] == 'complete')
    cases = ('broken link', 'missing anchor', 'duplicate identity', 'missing source', 'incomplete coverage')
    for case in cases:
        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp) / 'catalog'
            shutil.copytree(root, fixture, ignore=shutil.ignore_patterns('*.pdf', '__pycache__'))
            landing = fixture / 'patterns' / slug / 'README.md'
            if case == 'broken link':
                with landing.open('a') as out:
                    out.write('\n[Broken](missing.md)\n')
            elif case == 'missing anchor':
                with landing.open('a') as out:
                    out.write('\n[Broken](README.md#missing-heading)\n')
            elif case == 'duplicate identity':
                shutil.copytree(landing.parent, fixture / 'patterns' / 'duplicate')
            elif case == 'missing source':
                page = landing.parent / 'solution.md'
                page.write_text(re.sub(r'^Source: .*$', '', page.read_text(), flags=re.M))
            else:
                data = json.loads((fixture / 'inventory.json').read_text())
                data[0]['status'] = 'pending'
                (fixture / 'inventory.json').write_text(json.dumps(data))
            errors = check(fixture, complete=(case == 'incomplete coverage'))
            expected = {'duplicate identity': 'duplicate canonical identity', 'missing source': 'missing source reference', 'incomplete coverage': 'incomplete pattern'}.get(case, case)
            assert any(expected in error for error in errors), (case, errors)
    print('Self-test passed: valid catalog and 5 deliberately invalid temporary catalogs.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--complete', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    if args.self_test:
        self_test(root)
    errors = check(root, args.complete)
    if errors:
        print('\n'.join(errors))
        return 1
    rows = json.loads((root / 'inventory.json').read_text())
    print(f'PASS: {sum(r["status"] == "complete" for r in rows)}/{len(rows)} patterns; '
          f'{len(list(root.rglob("*.md")))} Markdown files; links, anchors, reachability, identity, aspects and sources.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
