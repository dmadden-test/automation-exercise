import os

from behave import *
import requests

from features.config.config import logger, get_settings
from features.config.utils import verify_data_structure, validate_json_data, get_project_root
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


@then("i receive a valid HTTP {expected_status_code} response code")
def step_impl(context, expected_status_code: int):
    response = context.response.json()
    actual_status_code = int(response['responseCode'])
    expected_status_code = int(expected_status_code)

    assert actual_status_code == expected_status_code, f"Expected: {expected_status_code}, Received: {actual_status_code}"


@step("a valid {list} response body is received")
def step_impl(context, list: str):
    response_json = context.response.json()
    returned_list = response_json[f'{list}']
    # verify_data_structure(returned_list)
    test_path = os.path.join(get_project_root(), "data/")
    file_name = os.path.join(test_path, get_settings().FLOWS[list])
    validate_json_data(returned_list, file_name)

    assert returned_list is not None


@when("i send a {method} request to the {request} endpoint")
def step_impl(context, method: str, request: str):
    # Dynamically select the method from the requests module
    try:
        request_method = getattr(requests, method.lower())
    except AttributeError:
        raise ValueError(f"Invalid HTTP method: {method}")
    context.response = request_method(BASE_URL + f'{request}', verify=False)

    assert context.response is not None


@step("i receive an expected {code} response message")
def step_impl(context, code: str):
    actual_message = context.response.json()["message"]
    if code == '400':
        expected_message = "Bad request"
        # , search_product parameter is missing in POST request."
    else:
        expected_message = "This request method is not supported."

    logger.info(f"The actual message is: {actual_message}")
    assert expected_message in actual_message, f"Expected {expected_message} message, actual {actual_message}"


@when("i send a post request to the search products endpoint with '{search_parameter}'")
def step_impl(context, search_parameter: str):
    payload = {'search_product': f'{search_parameter}'}
    context.response = requests.post(BASE_URL + 'searchProduct', data=payload, verify=False)

    assert context.response is not None


@step("results related to '{search_parameter}' are returned")
def step_impl(context, search_parameter: str):
    response = context.response.json()["products"]
    if response == '[]':
        logger.info(f"No search results for '{search_parameter}'")
        return
    for item in response:
        search_result = item['category']['category']
        assert search_parameter in search_result, f"No search results for '{search_parameter}'"
