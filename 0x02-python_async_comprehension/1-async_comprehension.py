#!/usr/bin/env python3
"""
Module 1-async_comprehension
This module contains a coroutine called async_comprehension
that collects 10 random numbers from the async_generator
using an asynchronous comprehension.
"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers asynchronously
    from the async_generator using an asynchronous comprehension.

    Returns:
        A list of 10 random float numbers between 0 and 10.
    """
    return [i async for i in async_generator()]
