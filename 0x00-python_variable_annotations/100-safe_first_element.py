#!/usr/bin/env python3
"""Duck typing first element of a sequence
"""

from typing import Sequence, Any, Optional

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely returns the first element of a sequence or None if the sequence is empty.

    Args:
        lst (Sequence[Any]): A sequence (e.g., list, tuple) containing elements of any type.

    Returns:
        Optional[Any]: The first element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
