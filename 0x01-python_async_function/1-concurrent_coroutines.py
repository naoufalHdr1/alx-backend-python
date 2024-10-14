#!/usr/bin/env python3
"""
This module defines an asynchronous function wait_n that spawns wait_random
n times with the specified max_delay, and returns the list of delays in
ascending order.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns
    a list of all the delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(await delays)
