#!/usr/bin/env python3

"""
    Module for a testing classes
"""

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map
from typing import Union


class TestAccessNestedMap(TestCase):
    """
        Tests the access_nested_map function
        on different situations
    """

    @parameterized.expand([
        ({'a': 1}, ('a',)),
        ({'a': {'b': 2}}, ('a',)),
        ({'a': {'b': 2}}, ('a', 'b'))
    ])
    def test_access_nested_map(self, nested_map, path):
        """
            tests that access_nested_map returns
            the right values
        """

        self.assertEqual(
                access_nested_map(nested_map, path),
                access_nested_map(nested_map, path))
