#!/usr/bin/env python3
"""
This module contains a function that rerurns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple """
    return (k, float(v**2))
