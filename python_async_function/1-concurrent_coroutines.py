#!/usr/bin/env python3
"""Module compiled wth Python3"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine that takes 2 arguments: n and max_delay.
    It will spawn wait_random n times with the specified max_delay.
    :param n: int - number of times wait_random will be called.
    :param max_delay: int - maximum delay wait_random can wait.
    Returns: list of all the delays, as floats, in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]

    unsorted_tasks = await asyncio.gather(*tasks)

    sorted_tasks = bubble_sort(unsorted_tasks)
    return sorted_tasks


def bubble_sort(lst: List[float], epsilon: float = 1e-9) -> List[float]:
    """
    Function that reproduce a Bubble sort algorithm to sort a list.
    :param lst: list - the list to be sorted
    :param epsilon: float - tolerance value for comparing floats
    Returns: the sorted list
    """
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (lst[j] - lst[j + 1]) > epsilon:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
