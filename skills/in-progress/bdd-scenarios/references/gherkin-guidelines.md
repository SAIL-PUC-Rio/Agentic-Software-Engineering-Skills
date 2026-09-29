# Gherkin construction rules

## Feature

- Title names a capability; the description (`As a / I want / So that`, or prose) states the business value or outcome, so it can be identified from the description alone (Q1).
- One feature per capability. Scenarios under it cover the behaviors the source decided; do not pad with undecided edge cases (record them as Unresolved behavior).

## Scenario

- One behavioral intention: one action, one observable outcome.
- Title states both, e.g. `Customer with an empty cart cannot check out`. A title that says only "Checkout" or "Happy path" fails Q6/Q7.
- Distinct from its siblings. Same flow with different data is a `Scenario Outline` with `Examples`, not copies.
- Independent: no scenario relies on another having run.

## Keywords and order (Integrous)

- `Given` - the context already true before the action. Not an action under test.
- `When` - the single action or event under test. Exactly one.
- `Then` - the observable outcome, verified. Not an action, not setup.
- `And` / `But` continue the preceding keyword only. Order is Given, When, Then; no `Given` after a `When`, no `When` after a `Then`.
- `Background` only for context every scenario in the feature shares.

## Steps

- Business language from `CONTEXT.md`, with the proper actor. One term per concept.
- Every step earns its place: drop steps and details that do not change the meaning (Q4, Q10).
- Unambiguous: no "properly", "correctly", "some", "appropriate"; give the concrete expected result the source states (Q12).
- `Then` steps assert something a person or external system can observe.

## Declarative over imperative

Say what happens, not how it is driven.

```gherkin
# Imperative (wrong): UI/transport mechanics
When the customer clicks "#checkout-btn"
And the frontend sends POST /api/v1/orders

# Declarative (right)
When the customer places the order
```

Use UI or HTTP detail only when that interaction is itself the agreed external requirement.

## Undecided behavior

Never write a `Then` for an outcome the source did not decide. Record it under `### Unresolved behavior` (what is missing, which scenario it blocks) and let the upstream decision-maker resolve it.
