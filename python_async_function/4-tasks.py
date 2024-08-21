#!/usr/bin/env python3
"""Module compiled wth Python3"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine that takes 2 arguments: n and max_delay.
    It will spawn wait_random n times with the specified max_delay.
    :param n: int - number of times wait_random will be called.
    :param max_delay: int - maximum delay wait_random can wait.
    Returns: list of all the delays, as floats, in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    unsorted_tasks = await asyncio.gather(*tasks)

    sorted_tasks = sorted(unsorted_tasks)
    return sorted_tasks
