# Passes the quality gate (all eight attributes PASS).
Feature: Order checkout
  As a customer
  I want to place an order for the items in my cart
  So that I receive what I selected and am charged once

  Scenario: Customer places an order for a non-empty cart
    Given the customer has a cart containing 2 items
    When the customer places the order
    Then an order is created with those 2 items
    And the customer is charged the cart total

  Scenario: Customer with an empty cart cannot place an order
    Given the customer has an empty cart
    When the customer places the order
    Then the order is rejected because the cart is empty
    And the customer is not charged

  Scenario Outline: Customer is told when a coupon is not valid
    Given the customer has a cart containing 1 item
    And the customer applies the coupon "<coupon>"
    When the customer places the order
    Then the customer sees the message "<message>"

    Examples:
      | coupon   | message            |
      | EXPIRED1 | Coupon has expired |
      | UNKNOWN  | Coupon not found   |

# Unresolved behavior: the outcome of a payment declined at charge time
# was not decided in the source, so no scenario is written for it.
