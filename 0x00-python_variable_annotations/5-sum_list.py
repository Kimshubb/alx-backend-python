#!/usr/bin/env python3
#takes a list of floats as args and returns a their sum as float
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of a list of floats.

    Parameters:
    input_list (List[float]): A list of float numbers.

    Returns:
    float: The sum of the list as a float.
    """
    return sum(input_list)
