#!/usr/bin/env python3

"""
This module demonstrates basic usage of asynchronous coroutines in Python.
"""

import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """
    An asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive) seconds.
    
    Args:
        max_delay (float): The maximum delay value in seconds. Defaults to 10.

    Returns:
        float: The generated random delay value.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main() -> None:
    """
    The main entry point of the program that demonstrates the usage of the wait_random coroutine.
    """
    print(await wait_random())
    print(await wait_random(5))
    print(await wait_random(15))


if __name__ == "__main__":
    asyncio.run(main())
