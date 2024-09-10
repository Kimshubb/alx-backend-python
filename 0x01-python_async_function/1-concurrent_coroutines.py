#!/usr/bin/env python3
"""
Executes wait_random n times
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times
    """
    delays = []
    
    # Create tasks for wait_random, each time waiting for a random delay
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    
    # Use asyncio.as_completed to get tasks as they finish
    for task in asyncio.as_completed(tasks):
        delay = await task  # Await the finished task
        delays.append(delay)  # Collect the delay

    return delays
