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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that public_repos returns the correct list of repository names.
        """
        # Define the payload returned by the mocked `get_json`
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = mock_payload

        # Patch `_public_repos_url` and set its return value
        with patch.object(
                GithubOrgClient,
                '_public_repos_url',
                new_callable=PropertyMock,
                return_value="https://api.github.com/orgs/test-org/repos"
        ) as mock_public_repos_url:
            client = GithubOrgClient("test_org")

            # Call `public_repos` and verify the result
            repos = client.public_repos()
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(repos, expected_repos)

            mock_get_json.assert_called_once_with(
                    "https://api.github.com/orgs/test-org/repos"
            )
            mock_public_repos_url.assert_called_once()


if __name__ == "__main__":
    unittest.main()
