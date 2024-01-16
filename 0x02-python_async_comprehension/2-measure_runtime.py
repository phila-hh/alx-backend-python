#!/usr/bin/env python3
"""
2-measure_runtime module
"""
import asyncio
import time
from importlib import import_module


async_comp = import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ returns the execution time """
    start = time.time()
    await asyncio.gather(*(async_comp() for _ in range(4)))
    return time.time() - start
