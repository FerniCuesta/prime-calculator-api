Feature: Prime Discount Validation
  As a Marketing Manager
  I want to verify if a number is prime
  So that I can offer special discounts on prime-numbered days

  Scenario: A prime number qualifies for a discount
    Given the input number is 13
    When I check the prime status
    Then the result should be "Prime"
    And the discount eligibility should be "Eligible"

  Scenario: A non-prime number does not qualify
    Given the input number is 10
    When I check the prime status
    Then the result should be "Not Prime"
    And the discount eligibility should be "Not Eligible"