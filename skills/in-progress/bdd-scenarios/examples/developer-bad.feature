# Violates several attributes; each finding is annotated. Developer-facing.
Feature: Deduplication  # Unique/Q1 REVISE: no description, capability and value not identifiable

  Scenario: Dedup works  # Singular/Q6,Q7 REVISE: title names neither stimulus nor outcome
    Given the DedupService bean is constructed with a HashMap<String, Record>   # Focused/Q11 REVISE: private structure; Essential/Q10 REVISE
    And the user opens the catalog page       # Ubiquitous/Q9 REVISE: end-user actor for an internal stage; Essential/Q4 REVISE
    When dedupe() calls buildIndex() then iterates the map and calls putIfAbsent   # Focused/Q11 REVISE: algorithm, not "what"
    And the stage rejects records without a SKU   # Singular REVISE: second independent When
    Then the records are processed correctly  # Clear/Q12 REVISE: vague
    Given two records share SKU "A-100"        # Integrous/Q8 REVISE: Given after Then
    And the map size is 1                      # Focused/Q11 REVISE: asserts internal state, not interface

  Scenario: Dedup works again  # Unique/Q5 REVISE: near-duplicate of the scenario above
    Given two records share SKU "A-100"
    When dedupe() runs
    Then the records are processed correctly

# Complete/Q2 REVISE: no scenario for a record without a SKU, which DS-004 decided.
