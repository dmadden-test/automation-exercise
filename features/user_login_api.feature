Feature: This feature covers Login API test scenarios from https://automationexercise.com/

  Background:
    Given email and password are set
    And a user has been created

  Scenario Outline: Login
    When i send a post request to the verify login endpoint with '<email>' and '<password>'
    Then i receive a valid HTTP 200 response code
    And i receive an expected 200 response message

    Examples:
      | email        | password |
      | test@test.ie | test1234 |

  @negative
  Scenario: Post request to verifyLogin endpoint without email parameter returns error
    When i send a post request to the verifyLogin endpoint
    Then i receive a valid HTTP 400 response code
    And i receive an expected 400 response message

  @negative
  Scenario: Delete request to verifyLogin endpoint returns error
    When i send a delete request to the verifyLogin endpoint
    Then i receive a valid HTTP 405 response code
    And i receive an expected 405 response message

  @negative
  Scenario Outline: Post request to verifyLogin endpoint with invalid details returns error
    When i send a post request to the verify login endpoint with '<email>' and '<password>'
    Then i receive a valid HTTP 404 response code
    And i receive an expected 404 response message

    Examples:
      | email | password |
      | test  | test     |
      | null  | null     |