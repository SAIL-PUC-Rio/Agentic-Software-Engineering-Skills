# Regression mode

For a **refactor with no agreed behavior change** to a component that already exists. The scenarios pin down its **current** behavior so the refactor can be checked against it (characterization). Same gate, same three statuses, same Gherkin discipline. Only the source and the meaning of "known" change. Basis: `.agents/adr/0004-regression-scenarios-specify-observed-behavior-from-cited-code.md`.

## Source: observed behavior, cited

- The source is the existing module: its code and its existing tests. Read both before drafting.
- Every scenario cites the existing test (name and file) or the code line that settles its `Then`, in a comment above the scenario. A scenario with no citation is not written.
- Prefer behavior an existing test already asserts. Behavior visible only in code is allowed when the code states it plainly (a documented error, an explicit branch); cite the line.
- Regression scenarios are developer-facing: load [developer-facing.md](developer-facing.md) for the boundary and vocabulary. The boundary is the module's interface, not its internals, and never the structure the refactor is about to change.

## Never invent a `Then`

- Untested branches, accidental behavior (ordering, timing, formatting no test or comment pins), and cases where code and tests disagree go under `### Unresolved behavior`, stating what is missing and which scenario it blocks. Do not guess, and do not treat "the code happens to do X" as a decision that X is wanted.
- A regression scenario claims only that the behavior is preserved, never that it is correct. Do not fix or improve behavior in the scenarios.
- If the scope is not stated (which surface the refactor can touch), report it as unresolved rather than characterizing the whole system.

## Output

Return the Gherkin with `# Regression of <module>` and `# Source: <test or code citations>` comments above the Feature, then `### Unresolved behavior` (omit if empty), then the one-line gate result per attribute, as in construct mode.

## Review

A regression scenario is reviewed like any developer-facing one. A `Then` whose source is not a cited existing test or code line is `REVISE` (Q2, Q12): move it to `### Unresolved behavior`.
