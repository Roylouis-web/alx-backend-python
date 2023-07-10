#!/usr/bin/env python3

'''
    An Asynchronous function called
    task_wait_n that is almost identical
    to wait_n function
'''

from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
        Module for an asynchronous function
        named task_wait_n
    '''

    array: List[float] = []

    for i in range(n):
        array.append(
                await task_wait_random(max_delay))

    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array
