Feature: APIs

  Scenario: Get a list of all products
    When i send a get productsList request
    Then i receive a valid HTTP 200 response code
    And a valid products response body is received

  Scenario: Post a request to the products list endpoint
    When i send a post request to the products list endpoint
    Then i receive a valid HTTP 405 response code
    And i receive an expected response message

  Scenario: Get a list of all brands
    When i send a get brandsList request
    Then i receive a valid HTTP 200 response code
    And a valid brands response body is received

  Scenario Outline: Search products
    When i send a post request to the search products endpoint with '<search_parameter>'
    Then i receive a valid HTTP 200 response code
#    And search results are returned

    Examples:
    | search_parameter |
    | Tops      |
    | Tshirts   |