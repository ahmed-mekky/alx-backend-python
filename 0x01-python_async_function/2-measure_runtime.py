#!/usr/bin/env python3
"""importance of async and await syntax in python async function"""
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime of the wait_n function"""
    start = asyncio.get_event_loop().time()
    await wait_n(n, max_delay)
    end = asyncio.get_event_loop().time()
    return (end - start) / n
