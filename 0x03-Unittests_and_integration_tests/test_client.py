#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value
        """
        # Mock response data for get_json
        mock_response = {"login": org_name}
        mock_get_json.return_value = mock_response

        client = GithubOrgClient(org_name)
        result = client.org

        # Assertions
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, mock_response)

    def test_public_repos_url(self):
        """
        Test that _public_repos_url returns the expected URL from org.
        """
        mock_payload = {
                "repos_url": "https://api.github.com/orgs/test-org/repos"
        }

        # Patch `GithubOrgClient.org` to return the mock_payload
        client = GithubOrgClient("test_org")
        with patch.object(
                GithubOrgClient,
                'org',
                new_callable=PropertyMock,
                return_value=mock_payload
        ):

            result = client._public_repos_url
            self.assertEqual(result, mock_payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
