#!/usr/bin/env python3
"""complex types - string and int/float to tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """complex types - string and int/float to tuple"""
    return (k, v * v)
