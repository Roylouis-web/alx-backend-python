#!/usr/bin/env python3

'''
    Module for a coroutine named async_generator
'''

from asyncio import sleep
from typing import Iterator
from random import uniform


async def async_generator() -> Iterator[int]:
    '''
        A coroutine named async_genrator
        that takes no argument and yields an integer
    '''

    i: int = 1

    while i <= 10:
        await sleep(1)
        yield uniform(0, 10)
        i += 1
