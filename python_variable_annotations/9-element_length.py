#!/usr/bin/env python3
"""Function types annotation"""
import typing


def element_length(
    lst: typing.Iterable[typing.Sequence],
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Returns a list of each element and its length"""
    return [(i, len(i)) for i in lst]
