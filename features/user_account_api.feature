Feature: This feature covers User Account API test scenarios from https://automationexercise.com/

  Background:
    Given email and password are set
    And a user has been created

  Scenario: Delete user account
    When i send a delete request to the deleteAccount endpoint including email and password
    Then i receive a valid HTTP 200 response code
    And i receive an expected 200 response message
      # Account doesnt exist

  Scenario: Create a new account
    When i send a post request to create a new account
    Then i receive a valid HTTP 201 response code
    And i receive an expected 201 response message

   #Missing info, wrong method, account already exists

#    @negative
#    Scenario: Required fields missing


  Scenario: Get user account details
    When i send a 'get' request to the 'getUserDetailByEmail' endpoint including email parameter
    Then i receive a valid HTTP 200 response code
    And the users details are returned

    # account doesnt exist



