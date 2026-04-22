"""
Task 3: Series expansion of ln(1+x) with statistics and visualization.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

import math
from pathlib import Path

import LB4.ui as ui
from LB4.Task3.series_calculator import SeriesCalculator


def run():
    """Run compute series, show stats, show plot."""
    save_dir = Path(__file__).parent

    while True:
        try:
            x = ui.read_float("Enter x (-1 < x <= 1): ", ranges=[(-1, 1 + 1e-9)])
            eps = ui.read_float("Enter eps (eps > 0): ", min=0)

            calc = SeriesCalculator(x, eps)
            approx, n = calc.calculate()
            exact = math.log(1 + x)

            ui.show_table(
                [(x, n, approx, exact, eps)],
                header=["x", "n", "F(x)", "Math F(x)", "eps"],
            )

            st = calc.statistics()
            print("\n[Statistics of series terms]")
            print(f"Mean:     {st['mean']:.6f}")
            print(f"Median:   {st['median']:.6f}")
            print(f"Mode:     {', '.join(f'{v:.4f}' for v in st['mode'][:3])}"
                  f"{'…' if len(st['mode']) > 3 else ''}")
            print(f"Variance: {st['variance']:.6f}")
            print(f"Std dev:  {st['std']:.6f}")

            calc.plot(approx, save_dir)

        except ValueError as exc:
            print(f"Error: {exc}")

        if ui.read_str("\nContinue? (y/n): ").lower() != "y":
            break
