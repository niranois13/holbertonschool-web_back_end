#!/usr/bin/env python3
"""Module compiled with Python3"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that returns a list of tuples where each tuple contains a
    string from the input list and its length.
    :param lst: iterable list that contains elements we want to calculate
    the length of.
    Returns: list of tuples containing elements as strings and their
    lengths as int.
    """
    return [(i, len(i)) for i in lst]
