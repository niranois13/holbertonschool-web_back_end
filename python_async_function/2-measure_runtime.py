#!/usr/bin/env python3
"""Module compiled wth Python3"""

import asyncio
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function that measures the total execution time for wait_n(n, max_delay).
    :param n: int - number of times 'wait_random' will be called.
    :param max_delay: int - maximum delay 'wait_random' can wait.
    Returns: float - total elapsed time for 'wait_n' to be executed.
    """
    time_start = time()
    asyncio.run(wait_n(n, max_delay))
    time_end = time()

    return (time_end - time_start) / n
