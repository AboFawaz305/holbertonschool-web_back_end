#!/usr/bin/env python3
"""Function types annotation"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a functions that multiply with multiplier"""

    def mult(x: float) -> float:
        return x * multiplier

    return mult
