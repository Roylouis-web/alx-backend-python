#!/usr/bin/env python3

"""
    Module for an annotated function named zoom_array
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
        a type-annotated function named zoom_array
        with the parameters lst of type tuple and
        factor of type int and a return value of tuple
    """

    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
