#!/usr/bin/env python3
"""importance of async and await syntax in python async function"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """async function"""
    delays = [await task_wait_random(max_delay) for i in range(n)]
    return sorted(delays)
