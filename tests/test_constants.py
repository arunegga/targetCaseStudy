import unittest
from src.constants.constants import REDIS_HOST, REDIS_PORT, REDIS_DB, API_URL, API_KEY

class TestConstants(unittest.TestCase):

    def test_redis_constants(self):
        self.assertEqual(REDIS_HOST, 'localhost')
        self.assertEqual(REDIS_PORT, 6379)
        self.assertEqual(REDIS_DB, 0)

    def test_api_constants(self):
        self.assertEqual(API_URL, 'https://redsky-uat.perf.target.com/redsky_aggregations/v1/redsky/case_study_v1')
        self.assertEqual(API_KEY, '3yUxt7WltYG7MFKPp7uyELi1K40ad2ys')

if __name__ == '__main__':
    unittest.main()
