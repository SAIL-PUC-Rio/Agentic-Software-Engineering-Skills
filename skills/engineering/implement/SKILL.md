---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

Use /tdd where possible, at pre-agreed seams.

If the ticket or spec names `BS-###` scenarios, each one is a behavior to drive through /tdd: the Given/When/Then sets the observable behavior of a red-green slice, exercised at the seam the spec's Testing Decisions assigns to that BS ID (or the pre-agreed seam if none is assigned); a `developer-facing` BS is driven at the unit or module seam that line assigns, not through the UI. The scenario is not itself the test; write the test at the seam. Story IDs are for tracing only. Read the scenarios, never a story's wording, for what to build. If `bdd-scenarios` is installed, read its `references/during-implementation.md` when a slice needs a developer-facing scenario for a customer-facing BS: derive it from the parent BS, cite the `BS-###`, add no behavior; a case you find that the BS never settles is reported as unresolved and asked, never written or decided. It is a reference, not invoked by default, and everything works the same without it. Skip any `### Unresolved behavior` — ask the user rather than guess. A `**Kind:** regression` BS is a constraint, not a feature: the behavior already exists, so it must pass before and after your change, and you never edit a pre-existing test to make it pass; if one seems wrong, stop and ask. When refactoring an existing component and `bdd-scenarios` is installed, its regression mode pins the current behavior before you touch the code. A ticket or spec with no BS IDs (legacy `## User Stories`, or no stories) works as before: drive the acceptance criteria.

Follow a CODING_STANDARDS.md if it exists, and respect ADRs in the area you're touching.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Commit your work to the current branch.

Once committed, run `/evidence` to close out — it publishes a factual evidence pack for this work to the configured issue tracker and reports its own result alongside the implementation result.
