#!/usr/bin/env python3

'''
    Module for an asynchronous
    function named wait_n
'''

from random import uniform
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
        An asynchronous function called wait_n
        that takes in 2 arguments: n and max_delay
    '''

    array: List[float] = []

    for i in range(n):
        array.append(await wait_random(max_delay))

    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1],  array[j]

    return array
