# Violates several attributes; each finding is annotated.
Feature: Checkout  # Unique/Q1 REVISE: no description, business value not identifiable

  Scenario: Checkout  # Singular/Q6,Q7 REVISE: title names neither action nor outcome
    Given the user is on the login page      # Essential/Q4 REVISE: removable; Ubiquitous/Q9 REVISE: "user" vs canonical "customer"
    When the user types "bob" in #username   # Focused/Q11 REVISE: UI mechanics, not "what"
    And the user clicks "#checkout-btn"      # Focused/Q11 REVISE
    And the user changes their shipping address   # Singular REVISE: second independent When
    Then it works properly                   # Clear/Q12 REVISE: vague, open to interpretation
    Given the cart has 2 items               # Integrous/Q8 REVISE: Given after Then
    And the frontend sends POST /api/v1/orders  # Focused/Q11 REVISE: transport detail, not in requirement

  Scenario: Checkout again  # Unique/Q5 REVISE: near-duplicate of the scenario above
    Given the user is on the login page
    When the user clicks "#checkout-btn"
    Then it works properly

# Complete/Q2 REVISE: no scenario for an empty cart, which the requirement decided.
