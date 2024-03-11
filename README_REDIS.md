docker exec -it redis sh
/data # redis-cli 
127.0.0.1:6379> hello
127.0.0.1:6379> keys *
127.0.0.1:6379> set name Vasyl
127.0.0.1:6379> get name
127.0.0.1:6379> setex surname 60 "really long string" 
127.0.0.1:6379> ttl surname
127.0.0.1:6379> flushdb
127.0.0.1:6379> select 1
127.0.0.1:6379> info
127.0.0.1:6379[3]> keys f*
127.0.0.1:6379[3]> keys ?h
127.0.0.1:6379[3]> keys ??h*
127.0.0.1:6379[3]> del hh ff

127.0.0.1:6379[3]> hset users:info2 name Vasyl2 surname Kartychak2
127.0.0.1:6379[3]> hset users:info name Vasyl surname Kartychak
127.0.0.1:6379[3]> hget users:info name
127.0.0.1:6379[3]> hgetall users:info





