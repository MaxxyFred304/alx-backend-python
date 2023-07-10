#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay=10):
    """
    An asynchronous coroutine that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

    Parameters:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
