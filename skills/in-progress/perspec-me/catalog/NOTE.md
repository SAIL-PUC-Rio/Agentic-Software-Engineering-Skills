# Catalog is read-only

This catalog is immutable reference material for the `perspec-me` skill. Do
not edit, translate, or re-scrape its contents during `perspec-me` use.
See [SOURCES.md](SOURCES.md) for attribution, license notes, and coverage.

## Checking links

The catalog's relative Markdown links (including PDF `#page=N` anchors) are
verified with a stdlib-only script:

```sh
python3 skills/in-progress/perspec-me/catalog/check-links.py
```

Run it after any change to the catalog tree. It exits non-zero and lists
every broken link if one is found, otherwise it reports zero broken links.
