#!/usr/bin/env python3
"""
This module contains a function to return the length of each element in
an iterable.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each element in the input iterable.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple
    contains an element from the input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
