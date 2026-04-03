"""
Task 1: Compute ln(1+x) via power series expansion.

Subject: IGI
Lab Work: 3
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 27.03.2025
"""

import math
import ui

MAX_ITER = 500
NANO_EPS = 1e-9


def series_terms(x: float):
    """
    Generator of successive terms of the series for ln(1+x).

    The n-th term equals (-1)^(n+1) * x^n / n.

    Args:
        x (float): argument, must satisfy x in (-1, 1]
    """
    n = 1
    x_power = x
    sign = 1

    while True:
        yield n, sign * x_power / n
        n += 1
        x_power *= x
        sign *= -1


def emit_table(
        x_val: float,
        eps_val: float,
        f_val: float
):
    """
    Yield table rows (x, n, F(x), sum, eps) until precision eps_val is reached
    or MAX_ITER iterations are exhausted.

    Args:
        x_val  (float): argument of the function
        eps_val (float): required precision
        f_val  (float): exact value computed via math.log
    """
    total = 0.0
    for n, term in series_terms(x_val):
        total += term
        eps_cur = abs(f_val - total)
        yield (x_val, n, f_val, total, eps_cur)
        if eps_cur < eps_val or n >= MAX_ITER:
            break


def run():
    """
    Entry point for Task 1.

    Reads x (|x| > 1) and eps from the user, computes ln(1+x)
    via series expansion, and displays an iteration table.
    """
    x_val = ui.read_float(
        "Enter x in (-1, 1]: ",
        ranges=[(-1 + NANO_EPS, 1 + NANO_EPS)],
    )
    eps_val = ui.read_float("Enter eps (0 to 1): ", min=NANO_EPS, max=1)

    f_val = math.log(1 + x_val)
    ui.show_table(emit_table(x_val, eps_val, f_val), ["x", "n", "f(x)", "sum", "eps"])
