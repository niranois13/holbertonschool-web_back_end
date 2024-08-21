#!/usr/bin/env python3
"""Module compiled wth Python3"""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    An async coroutine that runs 'async_comprehension' 4 times and then returns
    the total execution time as a float number.
    Returns: float - the total elapsed time
    """
    time_start = asyncio.get_event_loop().time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    time_end = asyncio.get_event_loop().time()
    return time_end - time_start
