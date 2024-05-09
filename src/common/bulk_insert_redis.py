import redis
from src.constants.constants import REDIS_HOST, REDIS_PORT, REDIS_DB


def bulk_insert_redis(r):

    # Dictionary containing key-value pairs to insert
    data = {
        '13860428': '{"value": 13.49,"currency_code":"USD"}',
        '54456119': '{"value": 17.80,"currency_code":"USD"}',
        '13264003': '{"value": 11.45,"currency_code":"USD"}',
        '12954218': '{"value": 24.99,"currency_code":"USD"}'
    }

    # Perform bulk insertion
    r.mset(data)

    # Close the Redis connection
    print((r.get('13860428')).decode('utf-8'))
    print(r.get('54456119'))
    print(r.get('13264003'))
    print(r.get('12954218'))
    r.close()
    return True


# r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
# bulk_insert_redis(r)
