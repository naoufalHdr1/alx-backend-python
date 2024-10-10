#!/usr/bin/env python3
"""
This module contains a function to convert a key and value into a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of an integer or float.

    Parameters:
    k (str): The key as a string.
    v (Union[int, float]): The value, which can be an integer or float.

    Returns:
    Tuple[str, float]: A tuple containing the string k and the square
    of v as a float.
    """
    return (k, float(v ** 2))
