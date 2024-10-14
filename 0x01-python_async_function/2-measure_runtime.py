#!/usr/bin/env python3
"""
This module defines a function to measure the runtime of the wait_n function.
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns the average time per execution.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        float: Average runtime per coroutine call.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
