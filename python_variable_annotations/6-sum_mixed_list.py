#!/usr/bin/env python3
"""Module compiled with Python3"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function used to sum up all elements of a list.
    This list can contain ints or floats and will return the sum as a float.
    :param mxd_lst: int or float - The list containing elements to add together
    Returns: float - the sum
    """
    return sum(mxd_lst)
