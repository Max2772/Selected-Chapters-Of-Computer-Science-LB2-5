"""
Task 3: Determine whether the string entered by the user is a valid
        hexadecimal number. No regular expressions are used.

Subject: IGI
Lab Work: 3
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 27.03.2025
"""

import ui

HEX_DIGITS = frozenset("0123456789abcdefABCDEF")


def is_hex_number(s: str) -> bool:
    """
    Check whether s represents a valid hexadecimal integer.

    Accepts an optional leading '0x' or '0X' prefix.
    An empty string (or a string containing only the prefix) returns False.
    No regular expressions are used.

    Args:
        s (str): string to test

    Returns:
        bool: True if s is a valid hexadecimal number, False otherwise
    """
    if not s:
        return False

    # Strip optional '0x' / '0X' prefix
    if s[:2] in ("0x", "0X"):
        s = s[2:]

    # Must have at least one hex digit after the prefix
    if not s:
        return False

    return all(c in HEX_DIGITS for c in s)


def run():
    """
    Entry point for Task 3.

    Reads a string from the user and reports whether it is a
    hexadecimal number.
    """
    st = ui.read_str("Enter string: ")

    if is_hex_number(st):
        print(f'"{st}" IS a valid hexadecimal number.')
    else:
        print(f'"{st}" is NOT a valid hexadecimal number.')
