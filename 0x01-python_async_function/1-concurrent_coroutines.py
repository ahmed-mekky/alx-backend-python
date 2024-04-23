#!/usr/bin/env python3
"""importance of async and await syntax in python async function"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """async function"""
    delays = [wait_random(max_delay) for i in range(n)]
    results = await asyncio.gather(*delays)
    return sorted(results)
