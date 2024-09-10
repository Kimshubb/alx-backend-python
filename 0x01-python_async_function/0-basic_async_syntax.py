#!/usr/bin/env python3
"""Task 0 
"""
import asyncio
import random

async def wait_random(max_delay: int 10) -> float:
    """
    Waits for a random number of secs
    """
    wait_time = random.uniform(0, max_delay)
    await ayncio.sleep(wait_time)
    return wait_time
