# During implementation

For a developer about to build (or change) a component for a customer-facing `BS-###` scenario. Working outside-in, you state what the component should do **before** writing it, as a developer-facing scenario flowing from the acceptance scenario (`docs/bdd/bdd_principles_unit_tests.md`, 2.3.7). You **derive** that scenario from the parent BS; you never decide behavior. `/tdd` stays the loop and keeps its pacing; this only informs what is written inside it.

## Derive the component scenario

- Before the red-green slice for a customer-facing BS, write the developer-facing scenario at the unit or module seam the spec's Testing Decisions line assigns to that BS ID (the pre-agreed seam if none is assigned). Load [developer-facing.md](developer-facing.md) for the boundary and vocabulary.
- Take the inputs, state, and observable outcome from the parent's Given/When/Then, restated in the component's own vocabulary. Nothing else is a source.
- The test is the executable form of the scenario. A scenario that stays as a note is fine; one that has no test is not done.
- One scenario at a time, per slice. Never write every component scenario up front (`/tdd`'s horizontal-slicing rule stands).

## Trace to the parent

Put the parent in a comment above the Feature or Scenario, as in developer-facing.md: `# Parent: BS-004 (customer sees only distinct results)`. In the test, keep the same `BS-###` in a comment or the test name so the chain BS to scenario to test is readable.

## Shape the test

Name it for the one action and outcome (Q6, Q7). One behavioral intention, declarative steps, the component's own vocabulary, concrete expected values from the parent BS (Q9 to Q12). Run the existing 12-question gate on what you wrote; no new checks.

## No added behavior

A derived scenario adds no behavior beyond its parent BS. If you cannot trace a `Then` to a line of the parent, it does not get written.

## Unresolved

A case found while coding (an input class, error, or boundary the parent BS does not settle) is **not** a scenario and **not** something to decide. List it under `### Unresolved behavior`, stating what is missing and which scenario it blocks, and ask the user. Continue with the rest only if the case does not block the slice.

## Refactor phase

Changing an existing component with no behavior change: first pin its current behavior with [regression-mode.md](regression-mode.md), before touching code, and never edit a pre-existing test to make it pass.
