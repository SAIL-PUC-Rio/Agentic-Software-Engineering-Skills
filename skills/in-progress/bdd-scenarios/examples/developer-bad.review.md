# Recorded review of developer-bad.feature

Result of walking [developer-bad.feature](developer-bad.feature) through [review mode](../references/review-mode.md) with [developer-facing.md](../references/developer-facing.md). Source: the file plus the comment in it (DS-004 decided a missing-SKU case, stating no outcome); anything else is Unresolved.

## BDD Review

**Audience judged:** developer-facing (component vocabulary (stage, record, SKU, batch), parent comment BS-004/DS-004; the stray `user` is a misnamed actor, not a customer-facing signal)

### Findings

- **Essential - REVISE (Q4, Q10):** `the user opens the catalog page` is removable; the `HashMap<String, Record>` construction detail is removable.
- **Focused - REVISE (Q11):** `DedupService bean`, `buildIndex()`, `putIfAbsent`, and `the map size is 1` describe how the stage is built and its private state, not what it emits. Implementation detail leaks into Given, When and Then.
- **Singular - REVISE (Q6, Q7):** title `Dedup works` names neither stimulus nor outcome; two independent `When`s (deduplicate, reject a SKU-less record). Split.
- **Clear - REVISE (Q12):** `processed correctly` allows any interpretation. The only recoverable meaning is that records sharing a SKU collapse into one (from the `map size is 1` step).
- **Complete - REVISE (Q2, Q3):** no scenario for a record with no SKU. The file gives no outcome, so it is Unresolved, not invented.
- **Unique - REVISE (Q1, Q5):** no feature description; `Dedup works again` repeats the first scenario's Given/When/Then.
- **Ubiquitous - REVISE (Q9):** `user` is not an actor of an internal stage; the actor is the deduplication stage. Use its own terms (record, SKU, batch).
- **Integrous - REVISE (Q8):** `Given two records share SKU "A-100"` appears after `Then`.

### Revised scenario

```gherkin
# Parent: BS-004; source: DS-004
Feature: Duplicate removal in the catalog ingestion pipeline
  As the ingestion pipeline
  I want the deduplication stage to emit one record per product
  So that search results show each product once

  Scenario: Records sharing a SKU are merged into one
    Given the deduplication stage receives two records with SKU "A-100"
    When the stage processes the batch
    Then it emits one record with SKU "A-100"

  Scenario: A record without a SKU is rejected
    Given the deduplication stage receives a record with no SKU
    When the stage processes the batch
    # Then: unresolved, see below
```

`Dedup works again` is dropped as a duplicate of the first scenario.

### Unresolved behavior

- Outcome for a record with no SKU: blocks the rejection scenario (left as a stub without a `Then`).
- Feature value wording is inferred from the DS-004 comment; confirm with the source.
