#!/usr/bin/env python3
"""
This module contain a function to zooms in on an array by repeating each
element a specified number of times.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on an array by repeating each element a specified number
    of times.

    Args:
        lst (List[int]): The list to be zoomed.
        factor (int): The number of times to repeat each element.
        Default is 2.

    Returns:
        List[int]: A new list with each element repeated 'factor' times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
