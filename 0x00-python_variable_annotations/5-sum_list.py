#!/usr/bin/env python3
"""
This module contains a function that sums a list of floating-point numbers
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns the sum of the numbers in the input list """
    return float(sum(input_list))
