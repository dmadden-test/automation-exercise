import logging
from functools import lru_cache

from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Settings(BaseSettings):

    FLOWS: dict = {
        "products": "product_list_schema.json",
        "brands": "brand_list_schema.json",
    }


@lru_cache()
def get_settings():
    return Settings()
