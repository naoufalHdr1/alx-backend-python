#!/usr/bin/env python3
"""
Module for testing the access_nested_map function with various test cases.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the expected result for
        various inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """
        Test that access_nested_map raises a KeyError for invalid paths.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_key}'")


class TestGetJson(unittest.TestCase):
    """
    Test cases for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json returns the expected result for given URLs.
        """
        # Create a mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        # Assert the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)


class Memoize(unittest.TestCase):
    """
    Test case for the memoize decorator
    """

    def test_memoize(self):
        """
        Test that memoize returns the expected result and ensure it
        called once.
        """

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        instance = TestClass()

        with patch.object(
                TestClass, 'a_method', return_value=42
        ) as mock_method:
            result1 = instance.a_property
            result2 = instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
