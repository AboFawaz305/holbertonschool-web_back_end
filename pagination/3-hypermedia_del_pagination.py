#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
                    }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hyper index"""
        assert type(index) is int and index >= 0
        assert index < len(self.__dataset)
        assert type(page_size) is int and page_size > 0
        indexed_data = self.__indexed_dataset
        if indexed_data is None:
            return {
                "index": index,
                "next_index": 0,
                "page_size": page_size,
                "data": [],
            }
        data_keys = sorted(indexed_data.keys())
        valid_keys = [k for k in data_keys if k >= index]
        next_index = None
        try:
            next_index = valid_keys[page_size]
        except IndexError:
            pass
        valid_keys = valid_keys[:page_size]
        data = [indexed_data[k] for k in valid_keys]
        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index,
        }
