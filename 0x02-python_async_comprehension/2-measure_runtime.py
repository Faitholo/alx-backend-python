#!/usr/bin/env python3
"""A coroutine that will execute async_comprehension four times"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    returns the total runtime for 4 asynchronous comprehension running in
    parallel
    """
    start = time.perf_counter()
    result = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start
    return total_time
