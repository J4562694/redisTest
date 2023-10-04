from app.config import redisPath
import redis

redisCli= redis.StrictRedis(
    host= redisPath.host,
    port= redisPath.port,
    db= redisPath.db,
    password= redisPath.password,
    decode_responses=True
)