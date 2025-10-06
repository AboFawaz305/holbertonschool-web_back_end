#!/usr/bin/env python3
"""
Async/Await
"""
import asyncio
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_append(res: typing.List[float], max_delay: int):
    """Wait and append the result"""
    res.append(await wait_random(max_delay))


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """spawn wait_random n times and wait for its value"""
    res = []

    async with asyncio.TaskGroup() as tg:
        for _ in range(n):
            tg.create_task(wait_append(res, max_delay))
        return res


if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
