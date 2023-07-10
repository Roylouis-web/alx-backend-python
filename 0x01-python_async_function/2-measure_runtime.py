#!/usr/bin/env python3

'''
    Module for an async function
    named measure_time
'''

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
        An asynchronous function named measured_time
    '''

    cur_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - cur_time

    return elapsed_time / n
