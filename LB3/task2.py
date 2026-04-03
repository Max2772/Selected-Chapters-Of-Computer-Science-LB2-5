"""
Task 2: Count positive integers entered by the user.
        Loop terminates when the user enters 10.

Subject: IGI
Lab Work: 3
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 27.03.2025
"""

import ui


def count_positives(numbers: list[int]) -> int:
    """
    Count how many values in the sequence are strictly positive.

    Args:
        numbers (list[int]): sequence of integers

    Returns:
        int: number of positive integers
    """
    return sum(1 for x in numbers if x > 0)


def run():
    """
    Entry point for Task 2.

    Reads integers one by one; stops when the user enters 10.
    Prints how many of the entered numbers were positive.
    Note: the terminating value 10 itself is NOT counted.
    """
    numbers = []
    while True:
        xv = ui.read_int("Enter number (enter 10 to stop): ")
        if xv == 10:
            break
        numbers.append(xv)

    print(f"Count of positive numbers: {count_positives(numbers)}")
