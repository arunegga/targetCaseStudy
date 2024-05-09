import logging
import json
import requests
from src.common.get_price_from_redis import get_price_from_redis
from src.common.get_name_from_api import get_name_from_api

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_product_info(product_id):
    """
    Retrieves product information including name and current price.

    Args:
        product_id (int): The ID of the product to retrieve information for.

    Returns:
        dict: A dictionary containing product information including ID, name, and current price.
              If an error occurs, it returns a dictionary containing an error message.
    """
    try:
        # Make synchronous request to external API to get product name
        product_name = get_name_from_api(product_id)

        # Retrieve price information from Redis
        value_from_redis_json = get_price_from_redis(product_id)

        # Check if price information exists in Redis
        if value_from_redis_json is None:
            logger.warning(f'Price not found for product ID {product_id}')
            return {"error": "Product price not found"}

        # Deserialize price information
        value_from_redis = json.loads(value_from_redis_json)

        # Construct final response
        final_response = {"id": product_id, "name": product_name, "current_price": value_from_redis}
        return final_response

    except requests.exceptions.HTTPError as e:
        logger.exception(f'Error while making request to external API: {e}')
        return {"error": "Product not found"}

    except requests.exceptions.RequestException as e:
        logger.exception(f'Error while making request to external API: {e}')
        return {"error": "An error occurred while fetching product information"}

    except Exception as e:
        logger.exception(f'An unexpected error occurred: {e}')
        return {"error": "An unexpected error occurred"}


# Example usage:
# product_info = get_product_info(13860428)
# print(product_info)
