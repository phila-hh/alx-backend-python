#!/usr/bin/env python3
"""
0-async_generator module
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ generates 10 random numbers """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
