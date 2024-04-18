#!/usr/bin/env python3
"""python_variable_annotations"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """python_variable_annotations"""
    if lst:
        return lst[0]
    else:
        return None
