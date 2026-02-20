Feature: Find the next prime number
  As a user of the discount system
  I want to know what the next prime number is after my input
  So I know when my next discount will be

  Scenario: Find the prime after a non-prime number
    Given the input number is 10
    When I ask for the next prime number
    Then the result should be 11