#!/usr/bin/env python3
"""Module compiled wth Python3"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Helper function that returns a tuple containing a starting index
    and an ending index, useful for pagination
    :param page: int - page number to be indexed
    :param page_size: int - number of elements per page to be indexed
    Returns: tuple - contains the two indexes, as integers,
    for pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
