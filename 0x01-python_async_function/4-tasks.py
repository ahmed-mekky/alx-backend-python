#!/usr/bin/env python3
"""importance of async and await syntax in python async function"""
import asyncio
task_wait_random = __import__('3-tasks.py').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> float:
    """async function"""
    delays = [task_wait_random(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
