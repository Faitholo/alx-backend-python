#!/usr/bin/env python3
"""annotated function, takes floats as argument, returns sum as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum as float"""
    return sum(mxd_lst)
