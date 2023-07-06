#!/usr/bin/env python3

"""
    Module for a type annotated function named safely_get_value
"""

from typing import TypeVar, Union, Any, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
        An annotated function named safely_get_value
        with parameters dct: Mapping, key: Any, default:
        Typevar or None
    """

    if key in dct:
        return dct[key]
    else:
        return default
