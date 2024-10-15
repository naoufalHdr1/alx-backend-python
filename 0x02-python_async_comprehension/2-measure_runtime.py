#!/usr/bin/env python3
"""
Module 2-measure_runtime
This module contains a coroutine called measure_runtime that measures
the time taken to run async_comprehension four times in parallel.
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel.

    It measures the total runtime for the execution of the four coroutines.

    Returns:
        A float representing the total runtime in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
