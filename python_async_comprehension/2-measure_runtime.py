#!/usr/bin/env python3
"""Measure async"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure async_comprehension runtime"""
    start_time = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.perf_counter()
    return end_time - start_time


if __name__ == "__main__":

    async def main():
        return await measure_runtime()

    print(asyncio.run(main()))
