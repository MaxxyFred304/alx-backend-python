#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def main():
    tasks = [wait_random(), wait_random(5), wait_random(15)]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())

