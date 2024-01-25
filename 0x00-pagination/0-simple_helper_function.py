#!/usr/bin/env python3
"""func to contain definition of index_range helper"""
from typing import Tuple


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
