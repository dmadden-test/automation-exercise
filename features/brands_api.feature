Feature: This feature covers Brands API test scenarios from https://automationexercise.com/

  Scenario: Get a list of all brands
    When i send a get request to the brandsList endpoint
    Then i receive a valid HTTP 200 response code
    And a valid brands response body is received

  @negative
  Scenario: Put request to brandList endpoint returns error
    When i send a put request to the brandsList endpoint
    Then i receive a valid HTTP 405 response code
    And i receive an expected 405 response message