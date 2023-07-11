#!/usr/bin/env python3

'''
    Module for a coroutine named async_comprehension
'''

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
        A coroutine named async_comprehension
        that takes no parameter and returns a list
        of floats yielded by the async_generator
        coroutine
    '''

    return [i async for i in async_generator()]
