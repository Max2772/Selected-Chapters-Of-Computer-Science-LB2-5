"""
Task 4: Isosceles trapezoid — draw, fill, annotate, save.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

from pathlib import Path

import LB4.ui as ui
from LB4.Task4.trapezoid import Trapezoid

def run():
    """Read parameters, build trapezoid, show info and plot."""
    save_dir = Path(__file__).parent

    while True:
        try:
            a = ui.read_float("Enter bottom base a > 0: ", min=0.0)
            b = ui.read_float("Enter top base b > 0: ", min=0.0)
            h = ui.read_float("Enter height h > 0: ", min=0.0)
            color = ui.read_str("Enter color (e.g. blue, red): ")
            label = ui.read_str("Enter figure label: ")

            trap = Trapezoid(a, b, h, color)

            print(f"\n{trap}")

            ui.show_table(
                [(trap.a, trap.b, trap.h, trap.leg(), trap.area(), trap.color)],
                header=["a", "b", "h", "leg", "area", "color"],
            )

            trap.draw(label, save_dir)

        except ValueError as exc:
            print(f"Error: {exc}")

        if ui.read_str("\nContinue? (y/n): ").lower() != "y":
            break
