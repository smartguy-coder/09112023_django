import redis
from datetime import timedelta

r = redis.Redis(host='127.0.0.1', port=6379, db=3)

# r.set('new_gfnhfgnkey', 'new value')
# data_from_redis = r.get('new_key')
# print(data_from_redis)


# r.hset(
#     'users:1234',
#     mapping={
#         'name': 'Alex',
#         'surname': 'Alex 56565',
#         'age': 55
#     }
# )

# print(r.hgetall('users:1234')[b'age'])

# r.setex('new_key555', time=timedelta(seconds=10), value='new value')

print(r.ttl('new_key555'))
r.close()
