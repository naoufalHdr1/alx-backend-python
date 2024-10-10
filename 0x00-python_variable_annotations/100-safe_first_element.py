#!/usr/bin/env python3
"""
This module provides a utility function to safely retrieve the first
element from a sequence. If the sequence is empty, it returns None.
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists,
    otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
