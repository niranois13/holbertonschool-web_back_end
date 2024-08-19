#!/usr/bin/env python3
"""Module compiled with Python3"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Function used to add a list of floats and return their sum.
    :param input_list: list[float] - The list of floats to be added
    Returns: float - the sum of the floats of the input_list
    """
    return sum(input_list)
