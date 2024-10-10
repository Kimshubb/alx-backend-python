#!/usr/bin/env python3
'''Asynchronous Python
'''
from time import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Measure the total runtime of executing `async_comprehension` four times in parallel.
    
    Returns:
        float: Total execution time in seconds.
    '''
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start
