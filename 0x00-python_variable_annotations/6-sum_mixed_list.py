#!/usr/bin/env python3
"""
This module contains a function that sums a mixed list of int and float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns the sum of the numbers in the mixed list input  """
    return float(sum(mxd_lst))
