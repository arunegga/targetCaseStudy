import unittest
from unittest.mock import patch
import fakeredis
from src.common.bulk_insert_redis import bulk_insert_redis

class TestRedisFunctionality(unittest.TestCase):

    @patch('src.common.bulk_insert_redis.redis', fakeredis.FakeRedis)
    def test_redis_functionality(self):
        # Mocked Redis connection
        r = fakeredis.FakeRedis()

        # Perform the Redis operations
        r.mset({
            '13860428': '{"value": 13.49,"currency_code":"USD"}',
            '54456119': '{"value": 17.80,"currency_code":"USD"}',
            '13264003': '{"value": 11.45,"currency_code":"USD"}',
            '12954218': '{"value": 24.99,"currency_code":"USD"}'
        })

        # Call your function
        result = bulk_insert_redis(r)

        # Assert the results
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
