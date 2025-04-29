import json
from pathlib import Path

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


def get_project_root() -> Path:
    return Path(__file__).parent.parent