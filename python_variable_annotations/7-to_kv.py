#!/usr/bin/env python3
"""Union annotations"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Returns (k, v**2)"""
    return (k, v**2)
