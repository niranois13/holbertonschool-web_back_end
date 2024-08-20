#!/usr/bin/env python3
"""Module compiled wth Python3"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Function that waits for a random delay to return it.
    :param max_delay: int - native value of 10, upper born of the random delay
    Returns: float - the random delay defined by the function itself."""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay

