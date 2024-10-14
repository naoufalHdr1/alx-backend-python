#!/usr/bin/env python3
"""
This module defines a function that returns an asyncio Task.
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task
    that wraps the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The asyncio task wrapping wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
