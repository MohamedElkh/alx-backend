#!/usr/bin/env python3
"""func to define lass Server that paginates a database"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """func to contain definition of index_range helper
    args:
        page: the page number to return
        page_size: the number of items per page
    return:
        the res tuple
    """
    st, ed = 0, 0

    for x in range(page):
        st = ed
        ed += page_size
    return (st, ed)


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
        datal = len(datas)

        try:
            ind = index_range(page, page_size)
            return datas[ind[0]:ind[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        this function takes 2 int args and return a dict containing these
        Args:
            page: requested page
            page_size: number of items per page
        Return:
            res dict with key-value pairs
        """
        total = self.dataset()
        data = self.get_page(page, page_size)

        total_pages = math.ceil(len(total) / page_size)

        if data == []:
            page_size = 0

        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page > 1 else None

        new_info = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return new_info
