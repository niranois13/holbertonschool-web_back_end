#!/usr/bin/env python3
"""Module compiled wth Python3"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An async coroutine generator that will run 10times,
    each time waiting for 1 second and then yeild a float number.
    Yields : a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        random_number = random.uniform(0, 10)
        yield random_number
