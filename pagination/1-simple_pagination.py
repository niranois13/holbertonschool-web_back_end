#!/usr/bin/env python3
"""Module compiled wth Python3"""
import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Function that returns the data in the specified index range.
        :param page: int - page number to be indexed
        :param page_size: int - number of elements per page to be indexed
        Returns: List[List] - appropriate page of the dataset (list of rows)
        """
        assert isinstance(page, int) and page > 0, \
            "page must be an integer greater than 0."
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be an integer greater than 0."

        start_index, end_index = index_range(page, page_size)

        dataset = self.dataset()
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
