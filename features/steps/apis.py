import os

from behave import *
import requests

from features.config.config import logger, get_settings
from features.config.utils import (
    validate_json_data,
    get_project_root,
    create_new_user,
    get_http_attr,
)
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASSWORD = os.getenv("USER_PASSWORD")


@then("i receive a valid HTTP {expected_status_code} response code")
def step_impl(context, expected_status_code):
    try:
        response = context.response.json()
        actual_status_code = str(response.get("responseCode", None))
        logger.info(f"Actual Response Code: {actual_status_code}")

    except requests.exceptions.JSONDecodeError:
        actual_status_code = None
        logger.info(f"Response is not valid JSON")
        logger.error(f"Response content: {context.response.text}")

    except Exception as e:
        actual_status_code = None
        logger.error(f"An error occurred: {e}")

    if actual_status_code:
        assert (
            actual_status_code in expected_status_code
        ), f"Expected status code: {expected_status_code}, Received status code: {actual_status_code}."


@step("a valid {list} response body is received")
def step_impl(context, list: str):
    response_json = context.response.json()
    returned_list = response_json[f"{list}"]
    test_path = os.path.join(get_project_root(), "data/")
    file_name = os.path.join(test_path, get_settings().FLOWS[list])
    validate_json_data(returned_list, file_name)

    assert returned_list is not None


@when("i send a {method} request to the {request} endpoint")
def step_impl(context, method: str, request: str):
    """Dynamically select the method from the requests module"""
    request_method = get_http_attr(method, request)
    context.response = request_method(BASE_URL + f"{request}", verify=False)

    assert context.response is not None


@step("i receive an expected {code} response message")
def step_impl(context, code: str):
    expected_message = {
        "200": ["User exists!", "Account deleted!"],
        "201": "User created!",
        "400": [
            "Bad request, search_product parameter is missing in POST request.",
            "Bad request, email or password parameter is missing in POST request.",
            "Email already exists!",
        ],
        "404": [
            "User not found!",
            "Account not found with this email, try another email!",
        ],
        "405": "This request method is not supported.",
    }

    # Retrieve the expected message from the dictionary; if not found, use the default message
    expected = expected_message.get(code, "Unexpected message received")
    logger.info(f"Expected list of messages are: {expected_message}")

    response = context.response.json()
    logger.info(f"Response received is: {response}")

    actual_response = response.get("message", None)
    logger.info(f"Received message is: {actual_response}")

    assert actual_response in expected


@when("i send a post request to the search products endpoint with '{search_parameter}'")
def step_impl(context, search_parameter: str):
    payload = {"search_product": f"{search_parameter}"}
    context.response = requests.post(
        BASE_URL + "searchProduct", data=payload, verify=False
    )

    assert context.response is not None


@step("results related to '{search_parameter}' are returned")
def step_impl(context, search_parameter: str):
    response = context.response.json()["products"]
    if response == "[]":
        logger.info(f"No search results for '{search_parameter}'")
        return

    for item in response:
        search_result = item["category"]["category"]
        assert (
            search_parameter in search_result
        ), f"No search results for '{search_parameter}'"


@when(
    "i send a post request to the verify login endpoint with '{email}' and '{password}'"
)
def step_impl(context, email: str, password: str):
    payload = {"email": email, "password": password}
    context.response = requests.post(
        BASE_URL + "verifyLogin", data=payload, verify=False
    )

    assert context.response is not None


@when("i send a post request to create a new account")
def step_impl(context):
    context.execute_steps(
        """When i send a delete request to the deleteAccount endpoint including email and password"""
    )
    context.payload = create_new_user(context.email, context.password)
    context.response = requests.post(
        BASE_URL + "createAccount", data=context.payload, verify=False
    )

    assert context.response is not None


@when(
    "i send a delete request to the deleteAccount endpoint including email and password"
)
def step_impl(context):
    payload = {"email": context.email, "password": context.password}
    context.response = requests.delete(
        BASE_URL + "deleteAccount", data=payload, verify=False
    )

    assert context.response is not None


@when(
    "i send a '{request}' request to the '{endpoint}' endpoint including email parameter"
)
def step_impl(context, request: str, endpoint: str):
    payload = {"email": USER_EMAIL}
    request_method = get_http_attr(request, endpoint)

    context.response = request_method(
        BASE_URL + f"{request}", params=payload, verify=False
    )
    logger.info(f"The response text is: {context.response.text}")

    assert context.response is not None


@step("the users details are returned")
def step_impl(context):
    response = context.response.json()["user"]
    logger.info(f"The users details are returned: {response}")

    assert response is not None


@given("email and password are set")
def step_impl(context):
    context.email = USER_EMAIL
    context.password = USER_PASSWORD


@step("a user has been created")
def step_impl(context):
    context.execute_steps("When i send a post request to create a new account")
