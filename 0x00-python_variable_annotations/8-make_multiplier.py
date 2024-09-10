#!/usr/bin/env python3
"""multiplier function
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Args:
        multiplier (float): The multiplier to use for the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float as input and returns
        the product of the input and the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies the given value by the multiplier.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The result of multiplying the value by the multiplier.
        """
        return value * multiplier

    return multiplier_function
