# myRetail  API

This API provides endpoints to retrieve product information from an external API and Redis cache.

## Contents

1. [Overview](#overview)
2. [Dependencies](#dependencies)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Endpoints](#endpoints)
6. [Examples](#examples)


## Overview

This project consists of the following files:

- `src/main_module.py`: Main application file containing Flask endpoints.
- `src/service/get_product.py`: Module to fetch product name and price and returns a final response
- `src/common/get_name_from_api.py`: Module to fetch product name from an external API.
- `src/common/get_price_from_redis.py`: Module to retrieve product price from Redis cache.
- `src/common/set_price_to_redis.py`: Module to set product price in Redis cache.
- `src/constants/constants.py`: Constants file containing API URLs, Redis host, port, and database information.
- `requirements.txt`: File containing Python dependencies.

## Dependencies

- Python 3.x
- Flask
- Redis
- Requests

## Setup

1. Extract the zip file named targetCaseStudy.zip and open in any IDE which supports python 3.12 (Pycharm preferred):

2. Install dependencies:
In the terminal run the following command

- `pip install -r requirements.txt`

3. Install redis server if not installed already.
In the terminal run the following command

- `brew install redis`

4. Start Redis server:
In the terminal run the following command

- `redis-server`

5. Add python path
In the terminal run the following command

- `export PYTHONPATH=/path/to/your/project:$PYTHONPATH`

4. Run bulk_insert_redis.py file to one time insert data into redis cache

- `python src/common/bulk_insert_redis.py`

4. Run the Flask application:

- `python src/main_module.py`


The API will be accessible at `http://localhost:5000`.

## Endpoints

- `GET /products/<int:id>`: Retrieves product information by product ID.
- `PUT /products/<int:id>`: Updates product information in Redis cache by product ID.

## Examples

### Example 1: Retrieve Product Information

curl -X GET http://localhost:5000/products/12954218


Response:

```json
{
  "current_price": {
    "currency_code": "USD",
    "value": 24.99
  },
  "id": 12954218,
  "name": "Kraft Original Mac and Cheese Dinner - 7.25oz"
}
```

### Example 2: Update Product Price

curl -X PUT -H "Content-Type: application/json" -d '{"value": 15.99, "currency_code": "USD"}' http://localhost:5000/products/12954218


Request Body:
```json
{
  "value": 15.99,
  "currency_code": "USD"
}
```
Response:
```json
{
  "message": "Value for key '12954218' updated successfully"
}
```
