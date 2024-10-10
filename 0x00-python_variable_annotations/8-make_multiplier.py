#!/usr/bin/env python3
"""
This module contains a function to create a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies a given float by
    the specified multiplier.

    Parameters:
    multiplier (float): The multiplier value.

    Returns:
    Callable[[float], float]: A lambda function that takes a float and
    returns its product with the multiplier.
    """
    return lambda x: x * multiplier
