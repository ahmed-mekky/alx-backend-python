#!/usr/bin/env python3
"""Takes a list of strings and returns a tuple of the string and its length."""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes a list of strings"""
    return [(i, len(i)) for i in lst]
