# Cloud application architecture patterns

An English reading catalog for *Cloud Application Architecture Patterns* by Kyle Brown, Bobby Woolf, and Joseph Yoder (first edition, 2025). Start with a short description, choose one pattern, then open only the aspect relevant to your design question.

- [Browse the pattern index](INDEX.md): one sentence per pattern, grouped by book chapter.
- [Source inventory and aliases](INVENTORY.md): membership, book pages, draft mappings, and discrepancies.
- [Sources and attribution](SOURCES.md): edition, page numbering, source precedence, and reuse notes.
- [Delivery checklist](CHECKLIST.md): the named pattern slices from issue #36.
- [Verification](VERIFICATION.md): checks and example reading paths.

The book list defines 75 canonical identities, including supporting patterns. Website drafts provide expanded material where available; cited book passages supply missing detail. This is a reference catalog in the in-progress bucket, not an installable skill.

Each pattern keeps its name and aliases on its landing page. Context, problem, forces, solution, sketch, results, consequences, related patterns, and examples have separate pages when supported. **Results** describes the resulting design; **consequences** describes benefits, liabilities, and new problems. The existing [section notes](pattern_folder_documents.md) define these distinctions. Explicit gaps replace empty pages.

Run `python3 check_catalog.py` for incremental coverage, `python3 check_catalog.py --complete` for full coverage, and `python3 check_catalog.py --self-test` to exercise deliberate failures. The checker uses only Python's standard library; Python 3.9 or newer is required. External sources are recorded separately from deterministic local checks.
