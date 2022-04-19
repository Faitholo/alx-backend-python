#!/usr/bin/env python3
"""A coroutine called async_generator that takes no arguments"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    async generator loops 10 times, wait 1 second each time,
    yield a random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
