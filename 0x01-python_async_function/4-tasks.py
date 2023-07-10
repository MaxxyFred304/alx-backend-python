#!/usr/bin/env python3
""" Multiple coroutines """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns a list of completed n tasks"""
    concurrent_tasks = [task_wait_random(max_delay)
                        for _ in range(n)]
    completed_tasks = []
    for task in asyncio.as_completed(concurrent_tasks):
        completed_tasks.append(await task)
    return completed_tasks
