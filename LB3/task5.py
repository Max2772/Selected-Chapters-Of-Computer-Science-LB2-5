"""
Task 5: Given a list of real numbers:
          • find the element with the maximum absolute value;
          • compute the sum of all elements located BEFORE the last
            positive element.
        The list can be entered manually or generated randomly.

Subject: IGI
Lab Work: 3
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 27.03.2025
"""

from randrow import random_row

import ui


def max_abs_element(lst: list[float]) -> float:
    """
    Return the element of *lst* that has the greatest absolute value.

    Args:
        lst (list[float]): non-empty list of numbers

    Returns:
        float: element with max |value|
    """
    return max(lst, key=abs)


def sum_before_last_positive(lst: list[float]) -> float:
    """
    Compute the sum of all elements that appear BEFORE the last positive
    element in *lst*.  Returns 0 if there is no positive element, or if
    the last positive element is at index 0.

    Args:
        lst (list[float]): list of numbers

    Returns:
        float: sum of elements before the last positive one
    """
    last_pos_idx = -1
    for i, x in enumerate(lst):
        if x > 0:
            last_pos_idx = i

    if last_pos_idx <= 0:
        return 0.0

    return sum(lst[:last_pos_idx])


def run():
    """
    Entry point for Task 5.

    Reads the list (manual input or random generation), then prints:
      • the element with the maximum absolute value;
      • the sum of elements before the last positive element.
    """
    raw = ui.read_float_list(
        "Enter list (numbers separated by spaces) "
        "or enter a single positive integer N to generate N random values: "
    )

    if len(raw) == 1 and raw[0] > 0 and raw[0] == int(raw[0]):
        lst = list(random_row(int(raw[0])))
        print("Generated random row:", lst)
    else:
        lst = raw

    max_abs = max_abs_element(lst)
    print(f"Element with max absolute value: {max_abs}")

    total = sum_before_last_positive(lst)
    print(f"Sum of elements before last positive: {total}")
