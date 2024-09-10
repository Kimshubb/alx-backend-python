#!/usr/bin/python3
"""6-sum_mixed_list.py
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list containing both integers and floats as a float.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
    float: The sum of the list as a float.
    """
    return sum(mxd_lst)
