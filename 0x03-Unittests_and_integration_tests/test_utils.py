#!/usr/bin/env python3

"""
    Module for a testing classes
"""

from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from utils import requests

class TestAccessNestedMap(TestCase):
    """
        contains methods that test the access_nested_map
        function
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

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
            Tests that access_nested_map raises an exception
            with the following parameters
        """

        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """
        Contains methods to test the get_json method
    """

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
            Test that get_json method returns the
            ecpected results
        """

        with patch('requests.get') as mocked_get:
            mocked_get(test_url).json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mocked_get.assert_called_with(test_url)


class TestMemoize(TestCase):
    """
        Contains a method that tests the memoize function
    """

    def test_memoize(self):
        """
            Tests that the memoize function returns
            the right output
        """

        class TestClass:
            """
                A test class
            """

            def a_method(self):
                """
                    A test method
                """
                return 42

            @memoize
            def a_property(self):
                """
                    A test method
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            mocked.return_value = 42
            temp = TestClass()
            self.assertEqual(temp.a_property, 42)
            self.assertEqual(temp.a_property, 42)
            mocked.assert_called_once()
