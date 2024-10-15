#!/usr/bin/env python3
"""
Module 0-async_generator
This module contains a coroutine called async_generator
that yields random numbers between 0 and 10 asynchronously.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that loops 10 times, asynchronously waits 1 second,
    and yields a random float between 0 and 10.

    Yields:
        A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
