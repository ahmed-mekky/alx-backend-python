#!/usr/bin/env python3
"""importance of async and await syntax in python async function"""
async_comprehension = __import__('1-async_comprehension').async_comprehension
import asyncio
import time


async def measure_runtime() -> float:
    """measure_runtime"""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end = time.perf_counter()
    return float(end - start)
