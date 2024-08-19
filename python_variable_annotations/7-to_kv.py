#!/usr/bin/env python3
"""Module compiled with Python3"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function used to join together, in a tuple, a string and the root square
    of an int or float.
    :param k: str - the string to be added to the tuple
    :param v: int or float - the number to be squared
    Returns: tuple - contains the string k and the square root of v, as a float
    """
    v = v ** 2
    return (k, v)
