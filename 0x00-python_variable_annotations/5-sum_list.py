#!/usr/bin/env python3
"""Sum of a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum of a list of floats"""
    sum = 0
    for item in input_list:
        sum += item
    return sum
