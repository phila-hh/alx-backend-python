#!/usr/bin/env pythin3
"""
test_utils module
"""
from parameterized import parameterized
from typing import Dict, Tuple, Union
import unittest
from unittest.mock import patch, Mock
from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    """ Tests the access_nested_map method """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """ Testes access_nested_map output """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """ Tests exception raising of access_nested_map """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test the get_json method """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload", False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """ Test output of get_jjson """
        attrs = {"json.return_value": test_payload}
        with patch("request.get": return_value=Mock(**attrs)) as r_get:
            self.assertEqual(get_json(test_url), test_payload)
            r_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Tests the memoize function """
    def test_memoize(self) -> None:
        """ Tests the output of memoize """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
            with patch.object(
                    TestClass,
                    "a_method",
                    return_value=lambda: 42,
                    ) as memo_function:
                test_class = TestClass()
                self.assertEqual(test_class.a_property(), 42)
                self.assertEqual(test_class.a_property(), 42)
                memo_function.assert_called_once()
