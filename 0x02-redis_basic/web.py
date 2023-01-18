#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests

count = 0
redis_store = redis.Redis()
'''The module-level Redis instance.
'''

def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    redis_store.set(f"cached:{url}", count)
    redis_store.incr(f"count:{url}")
    redis_store.setex(f"cached:{url}", 10, redis.Redis.get(f"cached:{url}"))
    return requests.get(url).text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
