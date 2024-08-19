#!/usr/bin/env python3
"""Module compiled with Python3"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier.
    :param multiplier: float - the number used to multiplie the elements
    of a callable function with
    Returns: the function
    """
    def function_multiplier(number: float) -> float:
        """
        Function used to multiplie a number with a multiplier
        :param number: float - the number to be multiplied with multiplier
        Returns: the result of the multiplication
        """
        return number * multiplier

    return function_multiplier
