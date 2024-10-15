# 0x02. Python - Async Comprehension

## Overview

This project explores Python's asynchronous programming features, focusing on **asynchronous generators** and **async comprehensions**. You'll learn how to create asynchronous generators, perform async comprehensions, and type-annotate your asynchronous functions and coroutines. By the end, you'll understand how to work with async comprehensions and apply them to run multiple tasks concurrently.

## Learning Objectives

By completing this project, you'll be able to:

- Write an `asynchronous generator`.
- Utilize `async comprehensions` to collect results from asynchronous operations.
- Measure the execution time of concurrent asynchronous tasks.
- Type-annotate generators and async functions for better code clarity and debugging.

## Project Tasks

### Task 0: Async Generator

**File:** `0-async_generator.py`

Write a coroutine called `async_generator` that loops 10 times, each time:

1. Asynchronously waits for 1 second.
2. Yields a random float number between 0 and 10.

You can use Python's `random` module to generate random numbers.

**Example Usage:**
```python
import asyncio
from 0-async_generator import async_generator

async def main():
    async for num in async_generator():
        print(num)

asyncio.run(main())
```

### Task 1: Async Comprehensions

**File:** `1-async_comprehension.py`

Write a coroutine called `async_comprehension` that collects 10 random numbers from `async_generator` using an async comprehension. Return these numbers as a list.

**Example Usage:**
```python
import asyncio
from 1-async_comprehension import async_comprehension

async def main():
    result = await async_comprehension()
    print(result)

asyncio.run(main())
```

### Task 2: Run Time for Four Parallel Comprehensions

**File:** `2-measure_runtime.py`

Write a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`. Measure the total runtime and return it.

**Key Point:**
- The expected runtime is approximately 10 seconds because each `async_comprehension` takes about 10 seconds to complete, but since they are run in parallel, the total runtime should be the same as that of a single execution.

**Example Usage:**
```python
import asyncio
from 2-measure_runtime import measure_runtime

async def main():
    runtime = await measure_runtime()
    print(f"Total runtime: {runtime} seconds")

asyncio.run(main())
```

## Resources

- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)\
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)\
- [Type-hints for Generators](https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3)
