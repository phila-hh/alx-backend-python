#!/usr/bin/env python3
"""
This module contains a function that multiplies a floating-point number
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier """
    return lambda x: x * multiplier
