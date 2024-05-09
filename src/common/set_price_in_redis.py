import logging
import redis
from src.constants.constants import REDIS_HOST, REDIS_PORT, REDIS_DB

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def set_price_in_redis(product_id, value):
    """
    Sets price information to Redis cache for a given product ID.

    Args:
        product_id (int): The ID of the product to set price for.
        value (str): The price information to be stored in Redis.

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    # Connect to Redis
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

    try:
        # Set value by key in Redis
        r.set(str(product_id), value)
        return True
    except Exception as e:
        logger.error(f"Error setting price to Redis for product ID {product_id}: {str(e)}")
        return False
    finally:
        # Close the Redis connection
        r.close()
