#!/usr/bin/env python3
"""func to contain class with methods for creating simple"""
import csv
import math
from typing import List, Tuple


index_range = __import__('0-simple_helper_function').index_range


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

    @staticm
    def func_assert(value: int) -> None:
        """func to assert to value is positive int
        args:
            value: the value to be asserted
        """
        assert type(value) is int and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """func to Takes 2 integer arguments and returns requested
        args:
            page: required page number. must be positive int
            page_size: the number of records per page
        return:
            res list of lists
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        datas = self.dataset()
        st, ed = index_range(page, page_size)

        try:
            data = datas[st:ed]
        except IndexError:
            data = []
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """func to return the page of dataset
        args:
            page: the page number
            page_size: the page size
        return:
            the res of list
        """
        total_pages = len(self.dataset())
        data = self.get_page(page, page_size)

        information = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= total_pages else None
        }
        return information
