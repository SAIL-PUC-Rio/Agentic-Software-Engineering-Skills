# Passes the quality gate (all eight attributes PASS). Developer-facing, regression.
# Regression of the deduplication stage ahead of a refactor; scope: its public interface only.
# Source: tests/dedup_test (existing suite), cited per scenario.
Feature: Deduplication stage behavior preserved across the refactor
  As the maintainer refactoring the deduplication stage
  I want its current observable behavior pinned down
  So that the refactor can be shown to preserve it

  # Source: dedup_test "merges records with same SKU"
  Scenario: Records sharing a SKU are merged into one
    Given the deduplication stage receives two records with SKU "A-100"
    When the stage processes the batch
    Then it emits one record with SKU "A-100"

  # Source: dedup_test "rejects record without SKU"
  Scenario: A record without a SKU is rejected
    Given the deduplication stage receives a record with no SKU
    When the stage processes the batch
    Then it rejects that record with the error "missing SKU"

# Unresolved behavior: the order of emitted records is not asserted by any existing
# test and the code does not state it, so no scenario is written for it.
