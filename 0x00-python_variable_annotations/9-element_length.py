#!/usr/bin/env python3
"""function that given an iterable of sequences, returns a list of tuples.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Given an iterable of sequences, returns a list of tuples.
    Each tuple contains a sequence from the input and its length.

    Args:
        lst (Iterable[Sequence]): An iterable where each item is a sequence (e.g., list, string).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
        a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
