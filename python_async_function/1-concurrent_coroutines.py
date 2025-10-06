#!/usr/bin/env python3
"""Async/Await"""
import asyncio
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """spawn wait_random n times and wait for its value"""
    res = []

    async def wait_append():
        """Wait and append the result"""
        nonlocal res
        res.append(await wait_random(max_delay))

    await asyncio.gather(*[wait_append() for _ in range(n)])
    return res


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
