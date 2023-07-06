#!/usr/bin/env python3

from typing import List

"""
    Module for a type-annotated function called sum_list
"""


def sum_list(input_list: List[float]) -> float:
    """
        a type-annotated function sum_list which takes
        a list input_list of floats as argument and
        returns their sum as a float
    """

    a: int = 0

    for num in input_list:
        a += num

    return a
