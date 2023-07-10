#!/usr/bin/env python3

'''
    Module for an asynchronous
    function names wait_random
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
        An asynchronous function named wait_random
        that takes in an integer argument (max_delay)
        with a default value of 10 and waits for a
        random delay between 0 and max_delay(included)
        and eventually returns it
    '''

    value: float = random.uniform(0, max_delay)
    await asyncio.sleep(value)

    return value
