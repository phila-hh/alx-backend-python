#!/usr/bin/env python3
"""
This module contains a annotated function
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ returns the length of an itterable sequence """
    return [(i, len(i)) for i in lst]
