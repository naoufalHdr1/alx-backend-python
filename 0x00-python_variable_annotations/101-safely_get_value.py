#!/usr/bin/env python3
"""
This module provides a function to safely retrieve a value from a
dictionary
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')
deft = Union[T, None]
retrn = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: deft = None) -> retrn:
    """
    Safely retrieves the value from a dictionary for the given key.
    """
    if key in dct:
        return dct[key]
    else:
        return default
