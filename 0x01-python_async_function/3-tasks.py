#!/usr/bin/env python3
"""function that takes an integer, returns a asyncio.Task"""
import time
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """
    takes max_delay as an argument and return asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
