Feature: This feature covers Products API test scenarios from https://automationexercise.com/

  Scenario: Get a list of all products
    When i send a get request to the productsList endpoint
    Then i receive a valid HTTP 200 response code
    And a valid products response body is received

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
  Scenario: Post to search products endpoint without specifying a search parameter
    When i send a post request to the searchProduct endpoint
    Then i receive a valid HTTP 400 response code
    And i receive an expected 400 response message

  @negative
  Scenario: Post request to productsList endpoint returns error
    When i send a post request to the productsList endpoint
    Then i receive a valid HTTP 405 response code
    And i receive an expected 405 response message
