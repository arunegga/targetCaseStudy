import unittest
from unittest.mock import patch, MagicMock
from src.common.get_price_from_redis import get_price_from_redis

class TestGetPriceFromRedis(unittest.TestCase):

    @patch('src.common.get_price_from_redis.redis.Redis')
    def test_get_price_from_redis_found(self, mock_redis):
        # Create a MagicMock instance to mock the behavior of Redis
        mock_redis_instance = MagicMock()

        # Set the return value for the get method of the mocked Redis instance
        mock_redis_instance.get.return_value = b'{"value": 10.0, "currency": "USD"}'

        # Configure the mock_redis class to return the mocked Redis instance
        mock_redis.return_value = mock_redis_instance

        # Call the function with a mocked product ID
        result = get_price_from_redis(12345)

        # Assert that the function returns the expected value
        self.assertEqual(result, b'{"value": 10.0, "currency": "USD"}')

    @patch('src.common.get_price_from_redis.redis.Redis')
    def test_get_price_from_redis_not_found(self, mock_redis):
        # Create a MagicMock instance to mock the behavior of Redis
        mock_redis_instance = MagicMock()

        # Set the return value for the get method of the mocked Redis instance
        mock_redis_instance.get.return_value = None

        # Configure the mock_redis class to return the mocked Redis instance
        mock_redis.return_value = mock_redis_instance

        # Call the function with a mocked product ID
        result = get_price_from_redis(12345)

        # Assert that the function returns None when no price information is found
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
