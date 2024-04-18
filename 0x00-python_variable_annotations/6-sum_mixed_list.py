#!/usr/bin/env python3

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    sum = 0
    for item in mxd_lst:
        sum += item
    return sum
