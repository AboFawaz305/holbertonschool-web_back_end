#!/usr/bin/env python3
"""Async/Await"""
import asyncio
import typing

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """spawn wait_random n times and wait for its value"""
    res = []

    async def wait_append():
        """Wait and append the result"""
        nonlocal res
        res.append(await task_wait_random(max_delay))

    await asyncio.gather(*[wait_append() for _ in range(n)])
    return res


if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
