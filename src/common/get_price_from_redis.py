import logging
import redis
from src.constants.constants import REDIS_HOST, REDIS_PORT, REDIS_DB

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_price_from_redis(product_id):
    """
    Retrieves price information from Redis cache for a given product ID.

    Args:
        product_id (int): The ID of the product to retrieve price for.

    Returns:
        bytes | None: The price information stored in Redis as bytes, or None if no price information is found.
    """
    # Connect to Redis
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

    # Retrieve value by key from Redis
    value_from_redis_json = r.get(str(product_id))

    # Close the Redis connection
    r.close()

    return value_from_redis_json

# Example usage:
# print(get_price_from_redis(13860428))
