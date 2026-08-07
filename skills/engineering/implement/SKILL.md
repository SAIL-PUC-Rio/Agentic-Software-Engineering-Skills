---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

Use /tdd where possible, at pre-agreed seams.

Follow a CODING_STANDARDS.md if it exists, and respect ADRs in the area you're touching.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Commit your work to the current branch.

Once committed, run `/evidence` to close out — it publishes a factual evidence pack for this work to the configured issue tracker and reports its own result alongside the implementation result.
