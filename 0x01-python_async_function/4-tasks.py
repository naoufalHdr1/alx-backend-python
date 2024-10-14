#!/usr/bin/env python3
"""
This module defines the task_wait_n function, similar to wait_n,
but using task_wait_random instead of wait_random.
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay.
    Return the list of all the delays in ascending order.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): Maximum delay for task_wait_random.

    Returns:
        list[float]: List of delays in ascending order.
    """
    delays = asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))
    return sorted(await delays)
