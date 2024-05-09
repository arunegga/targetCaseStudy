import json
import logging
from flask import Flask, jsonify, request
from src.service.getProduct import get_product_info
from src.common.set_price_in_redis import set_price_in_redis
from src.common.validations import is_integer

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Define endpoint for getting product information
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    """
    Endpoint to get product information by product ID.
    """
    # Validate if ID is an integer
    if is_integer(id):
        logger.info("Input is valid")
    else:
        logger.info("Input not accepted. Please provide a valid product id")

    # Get product information
    product_info = get_product_info(id)

    # Return product information
    if product_info:
        return jsonify(product_info), 200
    else:
        return jsonify({"error": "Product not found"}), 404


# Define endpoint for updating Redis value
@app.route('/products/<int:id>', methods=['PUT'])
def update_redis_value(id):
    """
    Endpoint to update Redis value with product information.
    """
    try:
        # Get JSON data from request
        data = request.get_json()

        # Check if JSON data is provided
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        # Update value in Redis
        set_price_in_redis(id, json.dumps(data))

        return jsonify({'message': f'Value for key "{id}" updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
