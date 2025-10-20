#!/usr/bin/env python3
"""
Inedex range
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the range index for a page"""
    return (page - 1) * page_size, page * page_size


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        si, ei = index_range(page, page_size)
        if self.dataset() is None:
            return []
        return self.dataset()[si:ei]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get a hyper"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        next_page = None
        prev_page = None
        total_pages = 0
        if self.dataset() is not None:
            total_pages = math.ceil(len(self.dataset()) / page_size)
            if 0 < page - 1 <= total_pages:
                prev_page = page - 1
            if page + 1 < total_pages:
                next_page = page + 1
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }


if __name__ == "__main__":
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
