import os

import redis
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv("../../.env")

database_url = os.environ["DATABASE_URL"]
redis_url = os.environ["REDIS_URL"]

engine = create_engine(database_url, pool_pre_ping=True)

with engine.connect() as connection:
    result = connection.execute(
        text("SELECT current_database()")
    ).scalar_one()

    print(f"PostgreSQL connected: {result}")

redis_client = redis.Redis.from_url(redis_url)
redis_client.ping()

print("Redis connected: PONG")
print("invikost infrastructure checks passed")