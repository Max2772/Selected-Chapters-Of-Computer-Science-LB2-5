"""
Task 5: NumPy matrix analysis — min row sum, even/odd index correlation.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

import numpy as np

import LB3.ui as ui


def _print_matrix(a: np.ndarray):
    """Print a 2-D integer matrix row by row."""
    print()
    for row in a:
        print("  " + "  ".join(f"{v:4d}" for v in row))
    print()


def _stats_block(label: str, data: np.ndarray):
    """Print mean / median / var / std for *data*."""
    print(f"[{label}]")
    print(f"mean   = {np.mean(data):.4f}")
    print(f"median = {np.median(data):.4f}")
    print(f"var    = {np.var(data):.4f}")
    print(f"std    = {np.std(data):.4f}")


def _analyze(a: np.ndarray):
    """Run all required analyses on matrix a."""

    n, m = a.shape

    # 1. Row sums -> minimum
    row_sums = a.sum(axis=1)
    min_sum = row_sums.min()
    min_row = int(row_sums.argmin())

    print("─" * 45)
    print("Row sums:")
    for i, s in enumerate(row_sums):
        marker = " <- min" if i == min_row else ""
        print(f"row {i}: {s}{marker}")
    print(f"\nMinimum row sum = {min_sum} (row {min_row})")

    # 2. Elements by index parity
    flat = a.flatten()
    idx = np.arange(flat.size)
    even_vals = flat[idx % 2 == 0]
    odd_vals = flat[idx % 2 == 1]

    print("\nElements with even flat indices:", even_vals)
    print("Elements with odd flat indices:", odd_vals)

    # 3. Statistics for each group
    print()
    _stats_block("even-index elements", even_vals)
    _stats_block("odd-index  elements", odd_vals)

    # 4. Pearson correlation between the two groups
    min_len = min(len(even_vals), len(odd_vals))
    if min_len >= 2:
        r = np.corrcoef(even_vals[:min_len], odd_vals[:min_len])[0, 1]
        print(f"\nCorrelation (even-index vs odd-index) = {r:.6f}")
    else:
        print("\nNot enough data to compute correlation.")

    print("─" * 45)


def run():
    """Entry point: read dimensions, generate matrix, analyse."""

    while True:
        try:
            n = ui.read_int("Rows n > 0: ", min=1)
            m = ui.read_int("Columns m > 0: ", min=1)

            a = np.random.randint(-100, 100, size=(n, m))
            print("\nGenerated matrix A[{},{}]:".format(n, m))
            _print_matrix(a)

            print("zeros({0},{0}):".format(min(n, m)), np.zeros((min(n, m), min(n, m)), dtype=int))
            print("arange slice a[0, :]:  ", a[0, :])
            print("universal ufunc abs(-a[0]):  ", np.abs(-a[0]))

            _analyze(a)

        except ValueError as exc:
            print(f"Error: {exc}")

        if ui.read_str("\nContinue? (y/n): ").lower() != "y":
            break
