#!/usr/bin/env python3
"""importance of async and await syntax in python async function"""
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure time"""
    start = asyncio.get_event_loop().time()
    asyncio.run(wait_n(n, max_delay))
    end = asyncio.get_event_loop().time()
    return (end - start) / n
