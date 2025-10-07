#!/usr/bin/env python3
"""Async/Await"""


import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure wait_n total time"""
    total_time = asyncio.run(wait_n(n, max_delay))

    return sum(total_time) / n


if __name__ == "__main__":
    print(measure_time(5, 9))
