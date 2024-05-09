import unittest
from unittest.mock import patch, Mock
from src.common.get_name_from_api import get_name_from_api

class TestGetNameFromApi(unittest.TestCase):

    @patch('src.common.get_name_from_api.requests')
    def test_get_name_from_api_success(self, mock_requests):
        # Mocking successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'data': {
                'product': {
                    'item': {
                        'product_description': {
                            'title': 'Mocked Product Name'
                        }
                    }
                }
            }
        }
        mock_requests.get.return_value = mock_response

        # Call the function with a mocked product ID
        product_name = get_name_from_api(12345)

        # Assert that the function returns the expected product name
        self.assertEqual(product_name, 'Mocked Product Name')

    @patch('src.common.get_name_from_api.requests')
    def test_get_name_from_api_failure(self, mock_requests):
        # Mocking failed API response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_requests.get.return_value = mock_response

        # Call the function with a mocked product ID
        with self.assertRaises(Exception):
            get_name_from_api(12345)

if __name__ == '__main__':
    unittest.main()
