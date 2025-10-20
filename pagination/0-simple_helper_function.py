#!/usr/bin/env python3
"""
Inedex range
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the range index for a page"""
    return (page - 1) * page_size, page * page_size
