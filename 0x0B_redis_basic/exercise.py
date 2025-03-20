#!/usr/bin/env python3
"""Redis module"""

import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


class Cache:
    def __init__(self):
        """Initialize a Cache instance and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the given data in Redis with a uuid key and returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """Retrieve the data from Redis, apply the optional conversion func"""
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def _decode_str(self, data: bytes) -> str:
        """Decode bytes to string using UTF-8."""
        return data.decode("utf-8")

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string from Redis."""
        return self.get(key, self._decode_str)

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis."""
        return self.get(key, int)

    def replay(self, method: Callable):
        """Display the history of calls of a particular function."""
        r = redis.Redis()
        m_name = method.__qualname__
        n_calls = r.get(m_name)
        try:
            n_calls = n_calls.decode('utf-8')
        except Exception:
            n_calls = 0
        print(f'{m_name} was called {n_calls} times:')

        ins = r.lrange(m_name + ":inputs", 0, -1)
        outs = r.lrange(m_name + ":outputs", 0, -1)

        for i, o in zip(ins, outs):
            try:
                i = i.decode('utf-8')
            except Exception:
                i = ""
            try:
                o = o.decode('utf-8')
            except Exception:
                o = ""

            print(f'{m_name}(*{i}) -> {o}')
