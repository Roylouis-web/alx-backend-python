#!/usr/bin/env python3

'''
    Module for a coroutine named measure_runtime
'''

from asyncio import gather
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
        A coroutine called measure_runtime
        that takes no argument a returns the
        total runtime of the async_comprehension
        coroutine
    '''

    initial_time = perf_counter()
    await gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    return perf_counter() - initial_time
