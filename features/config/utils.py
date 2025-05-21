import json
from pathlib import Path

import requests
from faker import Faker
from jsonschema import validate, ValidationError
from features.config.config import logger

def verify_data_structure(data):
    """Ensure JSON contains required keys"""
    required_keys = {'id', 'name', 'price', 'brand', 'category'}
    for product in data:
        if not required_keys.issubset(product.keys()):
            raise ValueError(f'Missing required keys in product: {product}')


def validate_json_data(json_data, path):
    """Compare JSON against defined schema"""
    with open(path, 'r', encoding='utf-8') as file:
        schema = json.load(file)
        try:
            validate(instance=json_data, schema=schema)
            logger.info("JSON response is valid according to the schema.")
        except ValidationError as e:
            logger.info(f"JSON validation error: {e.message}")


def create_new_user(email, password):
    fake = Faker()

    payload = {
        "name": fake.name(),
        "email": email,
        "password": password,
        "title": fake.bothify(text="###"),
        "birth_date": fake.date(),
        "birth_month": fake.month(),
        "birth_year": fake.year(),
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "Company": fake.bothify(text="#######"),
        "address1": fake.address(),
        "address2": fake.address(),
        "country": fake.country(),
        "zipcode": fake.postcode(),
        "state": fake.state(),
        "city": fake.city(),
        "mobile_number": fake.phone_number(),
    }
    logger.info(payload)
    return payload


def get_http_attr(method, request):
    try:
        request_method = getattr(requests, method.lower())
    except AttributeError:
        raise ValueError(f"Invalid HTTP method: {method}")

    return request_method


def get_project_root() -> Path:
    return Path(__file__).parent.parent