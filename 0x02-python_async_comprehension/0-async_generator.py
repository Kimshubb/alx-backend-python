#!/usr/bin/env python3
"""task 0
"""
import asyncio
import random

async def async_generator():
    """Loop 10 times, asynchronously wait 1 second, then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronous wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10

