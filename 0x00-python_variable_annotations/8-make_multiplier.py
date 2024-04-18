#!/usr/bin/env python3
"""Make a multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Make a multiplier"""
    def mul(a: float) -> float:
        return a * multiplier
    return mul
