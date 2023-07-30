#!/usr/bin/env python3

"""
    Module for a testing classes for the client.py module
"""

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
import client
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """
        A class that contains a method that tests
        the GithubOrgClient class
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, org):
        """
            tests the org property in the GithubOrgClient
            class
        """

        with patch('client.get_json') as mocked:
            temp = GithubOrgClient(org)
            mocked.return_value = {
                    "repos_url": temp.ORG_URL.format(org=org)
            }
            self.assertEqual(temp.org, mocked.return_value)
            mocked.assert_called_once_with(temp.ORG_URL.format(org=org))
