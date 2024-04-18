#!/usr/bin/env python3
"""python_variable_annotations"""
from typing import Any, Union, TypeVar, Mapping


T = TypeVar('T')
def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None]= None) -> Union[Any, T]:
    """python_variable_annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
