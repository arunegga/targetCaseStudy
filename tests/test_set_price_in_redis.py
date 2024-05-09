import unittest
from unittest.mock import patch, MagicMock
from src.common.set_price_in_redis import set_price_in_redis

class TestSetPriceInRedis(unittest.TestCase):

    @patch('src.common.set_price_in_redis.redis.Redis')
    def test_set_price_in_redis_success(self, mock_redis):
        # Create a MagicMock instance to mock the behavior of Redis
        mock_redis_instance = MagicMock()

        # Configure the mock_redis class to return the mocked Redis instance
        mock_redis.return_value = mock_redis_instance

        # Call the function with mocked arguments
        result = set_price_in_redis(12345, '{"value": 10.0, "currency": "USD"}')

        # Assert that the function returns True indicating success
        self.assertTrue(result)

        # Assert that the set method of the mocked Redis instance was called with the correct arguments
        mock_redis_instance.set.assert_called_once_with('12345', '{"value": 10.0, "currency": "USD"}')

    @patch('src.common.set_price_in_redis.redis.Redis')
    def test_set_price_in_redis_failure(self, mock_redis):
        # Create a MagicMock instance to mock the behavior of Redis
        mock_redis_instance = MagicMock()

        # Configure the mock_redis class to raise an exception when set method is called
        mock_redis_instance.set.side_effect = Exception('Mocked error')

        # Configure the mock_redis class to return the mocked Redis instance
        mock_redis.return_value = mock_redis_instance

        # Call the function with mocked arguments
        result = set_price_in_redis(12345, '{"value": 10.0, "currency": "USD"}')

        # Assert that the function returns False indicating failure
        self.assertFalse(result)

        # Assert that the set method of the mocked Redis instance was called with the correct arguments
        mock_redis_instance.set.assert_called_once_with('12345', '{"value": 10.0, "currency": "USD"}')

if __name__ == '__main__':
    unittest.main()
