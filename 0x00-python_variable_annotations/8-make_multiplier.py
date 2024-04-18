#!/usr/bin/env python3
"""Make a multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def mul(a: float) -> float:
        return a * multiplier
    return mul
