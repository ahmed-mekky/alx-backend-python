#!/usr/bin/env python3
"""importance of async and await syntax in python async function"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehensor"""
    return [i async for i in async_generator()]
