import logging
import requests
import pandas as pd
from src.constants.constants import API_URL, API_KEY

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_name_from_api(product_id):
    """
    Retrieves product name from an external API using the provided product ID.

    Args:
        product_id (int): The ID of the product to retrieve name for.

    Returns:
        str: The name of the product.
    """
    # Make API request to get product information
    prod_info = requests.get(f'{API_URL}?key={API_KEY}&tcin={product_id}')
    # Raise an exception if response status is not successful
    prod_info.raise_for_status()
    # Convert API response to JSON format
    prod_info = prod_info.json()

    # Convert JSON response to DataFrame
    prod_info_df = pd.json_normalize(prod_info)

    # Extract product name from DataFrame
    product_name = prod_info_df['data.product.item.product_description.title'].values[0]

    return product_name
