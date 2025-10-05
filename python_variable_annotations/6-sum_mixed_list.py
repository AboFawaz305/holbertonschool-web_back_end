#!/usr/bin/env python3
"""List functions"""
import typing


def sum_mixed_list(input_list: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of input_list elements"""
    return sum(input_list)
