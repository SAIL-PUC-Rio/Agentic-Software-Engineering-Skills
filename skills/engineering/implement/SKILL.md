---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

Use /tdd where possible, at pre-agreed seams.

If the ticket or spec names `BS-###` scenarios, each one is a behavior to drive through /tdd: the Given/When/Then sets the observable behavior of a red-green slice, exercised at the seam the spec's Testing Decisions assigns to that BS ID (or the pre-agreed seam if none is assigned). The scenario is not itself the test; write the test at the seam. Story IDs are for tracing only. Read the scenarios, never a story's wording, for what to build. Skip any `### Unresolved behavior` — ask the user rather than guess. A ticket or spec with no BS IDs (legacy `## User Stories`, or no stories) works as before: drive the acceptance criteria.

Follow a CODING_STANDARDS.md if it exists, and respect ADRs in the area you're touching.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Commit your work to the current branch.

Once committed, run `/evidence` to close out — it publishes a factual evidence pack for this work to the configured issue tracker and reports its own result alongside the implementation result.
