#!/usr/bin/env python3
"""
Async/Await
"""
import asyncio
import random


async def wait_random(max_delay: int) -> float:
    """Wait for a random time and return it"""
    time = random.random() * max_delay
    await asyncio.sleep(time)
    return time
