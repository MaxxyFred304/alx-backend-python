#!/usr/bin/env python3
""" Multiple coroutines """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns a list of completed n tasks"""
    concurrent_tasks = [asyncio.create_task(wait_random(max_delay))
                        for _ in range(n)]
    completed_tasks = []
    for task in asyncio.as_completed(concurrent_tasks):
        completed_tasks.append(await task)
    return completed_tasks
