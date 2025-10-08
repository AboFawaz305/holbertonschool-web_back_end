#!/usr/bin/env python3
"""Async/Await"""
import asyncio
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


# async def wait_random(x: int) -> float:
#     return 1.3


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create a wait_random task"""
    return asyncio.create_task(wait_random(max_delay))
