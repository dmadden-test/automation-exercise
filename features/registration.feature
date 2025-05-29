Feature: User can register via the UI

  @UI
  Scenario: User is able to register an account
    Given the user is on the homepage
    And the user selects the Signup/Login link
    When the user enters their details
    Then their account is created