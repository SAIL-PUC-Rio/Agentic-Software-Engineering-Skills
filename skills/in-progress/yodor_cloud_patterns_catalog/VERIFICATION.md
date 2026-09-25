# Verification

[Catalog](README.md) · [Source inventory](INVENTORY.md) · [Delivery checklist](CHECKLIST.md)

Audit date: **2026-09-19**. Scope: [issue #36](https://github.com/Esduard/skills/issues/36) and its existing implementation slices #37–#42. This records local implementation and validation; it is not a claim that a commit, push, or issue closure occurred.

## Scope to evidence

| Requirement | Result and evidence |
| --- | --- |
| Book membership and identity (#37) | PASS: all 76 entries on printed i–iv / PDF 3–6 map to 75 unique name-and-start-page pairs in [inventory.json](inventory.json); Repositories is the documented duplicate. |
| Edition and source precedence (#37) | PASS: title/copyright pages and list inspected; [source notes](SOURCES.md) record authors, edition, PDF page mapping, fingerprint, draft revision, retrieval date and reuse observations. |
| First complete reading path (#38) | PASS: [Event Sourcing](patterns/event-sourcing/README.md), confirmed on list ii / PDF 4, has independently readable aspects and return links. Circuit Breaker was excluded after checking membership. |
| Second shape, aliases and relationships (#39) | PASS: [Extract Component](patterns/extract-component/README.md) maps the facade aliases to one folder and links the authors’ figure. [Application Services](patterns/application-services/README.md#source-gaps) demonstrates explicit missing aspects without empty files. |
| Structural verification (#40) | PASS: checker validates targets, Markdown anchors, reachability, canonical identities, index/folder agreement, available and unavailable aspects, backlinks and source references. |
| Remaining named slices (#41) | PASS: all 73 entries 5.1–5.73 in the [checklist](CHECKLIST.md) are complete. [Incremental check results](slice-checks.txt) record a passing check after each addition. |
| Final reconciliation (#42) | PASS: 75 canonical folders, 666 aspect pages, nine explicit gaps and 749 Markdown documents; no pending entries or placeholder content. |
| Related navigation (#42) | PASS: in-scope relationships use canonical local links. Out-of-scope links, such as Circuit Breaker and Entity Comparator, are explicitly external. Relationships are directional source statements; no reciprocal links were invented. |
| Packaging boundary (#42) | PASS: reference material remains under in-progress; no installable skill, promoted docs, router behavior, or plugin manifest entry is added. |

## Repeatable local checks

From this directory:

```bash
python3 check_catalog.py --complete
python3 check_catalog.py --self-test
```

Final result: **PASS — 75/75 patterns; 749 Markdown files.** The self-test accepts the valid catalog and rejects five temporary variants: a missing file, a missing heading anchor, a duplicate canonical identity, a removed source reference, and incomplete inventory coverage. Its temporary copies exclude PDFs. The catalog’s nine recorded unavailable aspects pass without placeholder files.

The checker follows this catalog’s inline Markdown link format and ATX headings; it is not a general Markdown parser. It does not determine whether a paraphrase is faithful or an external source remains available. Those are separate audit activities. Compared with PerSpecML’s target-existence checker, this version additionally checks meaningful local anchors, source/back links and inventory coverage.

## Source audit

The final set of canonical name/start-page pairs was compared with every entry extracted from the supplied PDF list: equality passed, with 76 occurrences and 75 identities. The reader introductions are original paraphrases of those questions, except that the erroneous main-list Repositories question is superseded by its supporting-list entry and p. 215 discussion.

Spot-checks compared the introductions and expanded passages for Event Sourcing (list ii; pp. 289–298), Extract Component (list ii; pp. 535–542), Repositories (both entries on iv; p. 215), Columnar Database (list i; pp. 356–366), and Wrap the Monolith (supporting list iv; p. 518). The reconciliation also records singular/plural book headings, the optional facade in the final Extract Component pattern, the draft/book session-state distinction, and the columnar/wide-column ambiguity.

Fifty source-repository drafts were mapped to book identities; 25 patterns use book fallbacks. All 125 category Markdown pages other than README indexes were accounted for: 50 mapped pages and 75 remaining source pages, including one alternate Strangler Application draft and 74 noncanonical techniques, sidebars, or references. See [the remaining-source inventory](WEBSITE-ONLY.md).

Live verification is separate from local checks: **73/73 linked website URLs returned HTTP 200**, covering the homepage, the 50 mapped drafts, linked figures and four out-of-scope related patterns. The timestamp and individual results are in [source-checks.json](source-checks.json). Publisher and GitHub reference URLs were not part of that live sweep. Source text and the PDF were used for authoring but are not redistributed.

## Progressive reading traces

Each transition below was checked against a link in the file actually opened. Counts include Markdown, citations and navigation. Tokens are a rough character-count/4 estimate, rounded up, not tokenizer measurements. Reopening the same file is counted once in the table.

### Select by introduction

Catalog → index → Event Sourcing landing page.

| File opened | Words | Approx. tokens |
| --- | ---: | ---: |
| [README.md](README.md) | 226 | 446 |
| [INDEX.md](INDEX.md) | 1289 | 3112 |
| [patterns/event-sourcing/README.md](patterns/event-sourcing/README.md) | 122 | 280 |
| **Total unique files** | **1637** | **3838** |

### Read only one aspect

Event Sourcing landing page → problem → back to its landing page.

| File opened | Words | Approx. tokens |
| --- | ---: | ---: |
| [patterns/event-sourcing/README.md](patterns/event-sourcing/README.md) | 122 | 280 |
| [patterns/event-sourcing/problem.md](patterns/event-sourcing/problem.md) | 49 | 120 |
| **Total unique files** | **171** | **400** |

### Follow a related pattern and return

Extract Component landing page → related patterns → Replace as Microservice landing page → index → catalog.

| File opened | Words | Approx. tokens |
| --- | ---: | ---: |
| [patterns/extract-component/README.md](patterns/extract-component/README.md) | 148 | 326 |
| [patterns/extract-component/related-patterns.md](patterns/extract-component/related-patterns.md) | 87 | 203 |
| [patterns/replace-as-microservice/README.md](patterns/replace-as-microservice/README.md) | 125 | 288 |
| [INDEX.md](INDEX.md) | 1289 | 3112 |
| [README.md](README.md) | 226 | 446 |
| **Total unique files** | **1875** | **4375** |

The one-aspect path opens a 49-word problem page in addition to its 122-word landing page; it does not open the solution, consequences, source inventory, or other patterns. The relationship path opens the related target’s landing page without expanding its details. The index contains descriptions and links, so browsing it does not load the 666 aspect documents.

## Residual source limits

The website is a draft, not an authoritative inventory of the final book. Nine aspects have insufficient distinct source treatment and are explicitly unavailable; these are source gaps, not unfinished catalog slices. Short supporting passages are not expanded into invented full patterns. The book’s Repositories list error and the columnar terminology ambiguity remain documented rather than silently corrected as if the sources agreed. Editorial text diagrams are identified as adaptations; source figures are linked, not copied.
