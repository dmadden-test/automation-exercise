Feature: APIs

  Scenario: Get a list of all products
    When i send a get request to the productsList endpoint
    Then i receive a valid HTTP 200 response code
    And a valid products response body is received

  @wip
  Scenario: Verify Login with valid details
    When i send a post request to the verifyLogin endpoint
    Then i receive a valid HTTP 200 response code

  Scenario: Get a list of all brands
    When i send a get request to the brandsList endpoint
    Then i receive a valid HTTP 200 response code
    And a valid brands response body is received

  Scenario Outline: Search products
    When i send a post request to the search products endpoint with '<search_parameter>'
    Then i receive a valid HTTP 200 response code
    And results related to '<search_parameter>' are returned

    Examples:
      | search_parameter |
      | Tops             |
      | Tshirts          |
      | Tracksuit        |
      | Water            |
    
  @negative
  Scenario: Put request to brandList endpoint returns error
    When i send a put request to the brandsList endpoint
    Then i receive a valid HTTP 405 response code
    And i receive an expected 405 response message
    
  @negative
  Scenario: Post to search products endpoint without specifying a search parameter
    When i send a post request to the searchProduct endpoint
    Then i receive a valid HTTP 400 response code
    And i receive an expected 400 response message

  @negative
  Scenario: Post request to productsList endpoint returns error
    When i send a post request to the productsList endpoint
    Then i receive a valid HTTP 405 response code
    And i receive an expected 405 response message

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