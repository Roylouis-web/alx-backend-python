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

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_public_repos_url(self, org):
        """
            tests the _public_repos_url property
        """

        with patch.object(GithubOrgClient, "org") as mocked:
            temp = GithubOrgClient(org)
            mocked.return_value = {
                    "repos_url": temp.ORG_URL.format(org=org)
            }
            temp.org = mocked.return_value
            url = temp.ORG_URL.format(org=org)
            self.assertEqual(temp._public_repos_url, url)

    def test_public_repos(self):
        """
            Tests the public_repos method
        """

        with patch('client.get_json') as mocked1:
            with patch.object(
                    GithubOrgClient,
                    '_public_repos_url') as mocked2:
                temp = GithubOrgClient('org')
                mocked1.return_value = [{
                        "name": "Merchandise",
                        "repos_url": "https://github.com"
                }]
                mocked2.return_value = "https://github.com"
                temp._public_repos_url = mocked2()
                self.assertEqual(
                        temp.public_repos(),
                        [mocked1.return_value[0]["name"]])
                mocked1.assert_called_once()
                mocked2.assert_called_once()
