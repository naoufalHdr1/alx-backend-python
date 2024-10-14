# 0x01. Python - Async

## Description

This project focuses on asynchronous programming in Python, specifically using the `async` and `await` syntax with the `asyncio` library. It covers fundamental concepts of async programming, such as executing asynchronous tasks, running coroutines concurrently, and creating asyncio tasks. You'll also learn how to measure execution time and manage asynchronous tasks effectively.

The tasks in this project will help you grasp the essentials of async programming, starting with simple async functions and progressing to more complex concurrency management.

## Learning Objectives

By the end of this project, you should be able to:

- Understand the `async` and `await` syntax in Python.
- Execute an asynchronous program using `asyncio`.
- Run multiple coroutines concurrently.
- Create and manage asyncio tasks.
- Utilize the `random` module to introduce randomness into async functions.

## Project Structure

The project consists of the following tasks:

### Task 0: The basics of async

Write an asynchronous coroutine `wait_random` that takes an integer argument `max_delay` (default value: 10). The coroutine waits for a random delay between 0 and `max_delay` seconds and returns the delay.

**File:** `0-basic_async_syntax.py`

### Task 1: Execute multiple coroutines at the same time with async

Write an async routine `wait_n` that spawns `wait_random` n times with a specified `max_delay` and returns a list of the delays in ascending order without using `sort()`.

**File:** `1-concurrent_coroutines.py`

### Task 2: Measure the runtime

Write a function `measure_time` that measures the total runtime for executing `wait_n(n, max_delay)` and returns the average time per coroutine.

**File:** `2-measure_runtime.py`

### Task 3: Create asyncio tasks

Write a regular function `task_wait_random` that returns an asyncio.Task for the `wait_random` coroutine.

**File:** `3-tasks.py`

### Task 4: Execute multiple tasks

Write an async routine `task_wait_n` similar to `wait_n`, but uses `task_wait_random` to create tasks and collect the delays.

**File:** `4-tasks.py`

## Resources

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)\
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)\
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)
