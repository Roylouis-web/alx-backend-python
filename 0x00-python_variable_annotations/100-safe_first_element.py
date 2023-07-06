#!/usr/bin/env python3

"""
    Module for a type-annotated function name safe_first_element
"""

from typing import Sequence, Any, Union, Type


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        A type-annotated function name safe_first_element
        with a parameter name lst which is a sequence
        with value of type 'Any'
    """

    if lst:
        return lst[0]
    else:
        return None
