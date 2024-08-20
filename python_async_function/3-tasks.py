#!/usr/bin/env python3
"""Module compiled wth Python3"""

import asyncio
from time import time

wait_random = __import__('1-concurrent_coroutines').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes an integer max_delay and returns a asyncio.Task.
    :param max_delay: int - maximum delay 'wait_random' can wait.
    Returns: Task object representing scheduled tasks
    """
    return asyncio.create_task(wait_random(max_delay))
