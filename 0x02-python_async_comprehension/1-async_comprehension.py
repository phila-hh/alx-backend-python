#!/usr/bin/env python3
"""
1-async_comprehension module
"""
from typing import List
from importlib import import_module


async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ returns a list of 10 random float numbers """
    return [i async for i in async_generator]
