import os

from behave import *
import requests

from features.config.config import logger, get_settings
from features.config.utils import verify_data_structure, validate_json_data, get_project_root

BASE_URL = 'https://automationexercise.com/api/'


@when("i send a get {request} request")
def step_impl(context, request: str):
    context.response = requests.get(BASE_URL + f'{request}', verify=False)
    assert context.response is not None


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


@when("i send a post request to the products list endpoint")
def step_impl(context):
    context.response = requests.post(BASE_URL + 'productsList', verify=False)
    assert context.response is not None


@step("i receive an expected response message")
def step_impl(context):
    expected_message = "This request method is not supported."
    actual_message = context.response.json()['message']
    assert expected_message == actual_message, f"Expected {expected_message} message, actual {actual_message}"


@when("i send a post request to the search products endpoint with '{search_parameter}'")
def step_impl(context, search_parameter: str):
    payload = {'search_product': f'{search_parameter}'}
    context.response = requests.post(BASE_URL + 'searchProduct', data=payload, verify=False)
    assert context.response is not None
