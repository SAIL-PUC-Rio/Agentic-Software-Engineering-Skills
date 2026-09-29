# Passes the quality gate (all eight attributes PASS). Developer-facing.
# Parent: BS-004 "Customer sees each catalog item once in search results"; source: DS-004.
Feature: Duplicate removal in the catalog ingestion pipeline
  As the ingestion pipeline
  I want the deduplication stage to emit one record per product
  So that search results show each product once

  Scenario: Records sharing a SKU are merged into one
    Given the deduplication stage receives two records with SKU "A-100"
    When the stage processes the batch
    Then it emits one record with SKU "A-100"

  Scenario: The record with the latest update time is kept
    Given the deduplication stage receives records with SKU "A-100" updated at 10:00 and 11:00
    When the stage processes the batch
    Then the emitted record carries the 11:00 update time

  Scenario: A record without a SKU is rejected
    Given the deduplication stage receives a record with no SKU
    When the stage processes the batch
    Then it rejects that record with the error "missing SKU"
    And it emits every other record in the batch

# Unresolved behavior: how records with equal update times are ordered
# was not decided in DS-004, so no scenario is written for it.
