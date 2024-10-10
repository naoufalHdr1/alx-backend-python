#!/usr/bin/env python3
"""
This module contains a function to sum a mixed list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of integers and floats
    to be summed.

    Returns:
    float: The sum of the integers and floats in the list.
    """
    return sum(mxd_lst)
