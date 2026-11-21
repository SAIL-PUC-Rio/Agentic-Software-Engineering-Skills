# Recorded review of bad.feature

Result of walking [bad.feature](bad.feature) through [review mode](../references/review-mode.md). Source: the file only; no requirement text was supplied, so behavior beyond what the file states is Unresolved.

## BDD Review

**Audience judged:** customer-facing (business vocabulary, `customer` actor, UI and transport steps)

### Findings

- **Essential - REVISE (Q4, Q10):** `Given the user is on the login page` is removable; `And the frontend sends POST /api/v1/orders` is a removable detail.
- **Focused - REVISE (Q11):** `types "bob" in #username`, `clicks "#checkout-btn"` and the POST step are UI/transport mechanics; state the behavior (customer places the order).
- **Singular - REVISE (Q6, Q7):** title `Checkout` names neither action nor outcome; the scenario has two independent `When`s (place order, change shipping address). Split.
- **Clear - REVISE (Q12):** `Then it works properly` allows any interpretation. Meaning recoverable only from the POST step (an order is created), used as the cited basis.
- **Complete - REVISE (Q2, Q3):** no scenario for the empty cart. The file annotates it as decided but states no outcome, so it is Unresolved, not invented. Shipping-address change has no outcome either.
- **Unique - REVISE (Q1, Q5):** feature has no description; `Checkout again` is a subset of the first scenario (same Given/When/Then).
- **Ubiquitous - REVISE (Q9):** `user` vs canonical `customer`.
- **Integrous - REVISE (Q8):** `Given the cart has 2 items` appears after `Then`.

### Revised scenario

```gherkin
Feature: Order checkout
  As a customer
  I want to place an order for the items in my cart
  So that I receive what I selected

  Scenario: Customer places an order for a non-empty cart
    Given the customer has a cart containing 2 items
    When the customer places the order
    Then an order is created with those 2 items

  Scenario: Customer changes their shipping address
    When the customer changes their shipping address
    # Then: unresolved, see below
```

`Checkout again` is dropped as a duplicate of the first scenario.

### Unresolved behavior

- Outcome of checkout with an empty cart: blocks the empty-cart scenario.
- Outcome of changing the shipping address: blocks `Customer changes their shipping address` (left as a stub without a `Then`).
- Business value wording in the feature description is inferred from scenario content; confirm with the source.
