"""
Isosceles trapezoid model for Task 4.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

import math
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from LB4.Task4.color import Color
from LB4.Task4.shape import Shape


class Trapezoid(Shape):
    """
    Isosceles trapezoid with bases a, b and height h.
    """

    name = "Isosceles Trapezoid"

    def __init__(self, a: float, b: float, h: float, color: str):
        """
        Args:
            a (float): bottom base
            b (float): top base
            h (float): height
            color (str): fill color name
        """
        super().__init__()
        if a <= 0 or b <= 0 or h <= 0:
            raise ValueError("a, b and h must be positive.")
        self.a = a
        self.b = b
        self.h = h
        self.color_obj = Color(color)

    @staticmethod
    def validate_positive(value: float, name: str) -> float:
        """Raise ValueError if value is not positive."""
        if value <= 0:
            raise ValueError(f"{name} must be positive, got {value}.")
        return value

    @property
    def color(self) -> str:
        return self.color_obj.color

    @color.setter
    def color(self, value: str):
        self.color_obj.color = value

    @classmethod
    def get_name(cls) -> str:
        """Return the figure name."""
        return cls.name

    def area(self) -> float:
        """Area = (a + b) / 2 * h."""
        return (self.a + self.b) / 2 * self.h

    def leg(self) -> float:
        """Length of the lateral side."""
        return math.sqrt(self.h ** 2 + ((self.a - self.b) / 2) ** 2)

    def __str__(self) -> str:
        return (
            "{name} | color: {color} | "
            "a={a:.2f}, b={b:.2f}, h={h:.2f} | "
            "leg={leg:.2f} | area={area:.2f}\n"
        ).format(
            name=self.get_name(),
            color=self.color,
            a=self.a, b=self.b, h=self.h,
            leg=self.leg(),
            area=self.area(),
        )

    def _vertices(self) -> list[tuple]:
        """
        Return the four vertices centered on x=0.
        """
        return [
            (-self.a / 2, 0),
            (self.a / 2, 0),
            (self.b / 2, self.h),
            (-self.b / 2, self.h)
        ]

    def draw(self, label: str, save_dir: Path):
        """
        Draw the trapezoid, display it and save to <save_dir>/trapezoid.png.

        Args:
            label    (str):  annotation text
            save_dir (Path): directory for the output image
        """
        verts = self._vertices()
        xs = [v[0] for v in verts]
        ys = [v[1] for v in verts]

        fig, ax = plt.subplots(figsize=(7, 5))
        polygon = plt.Polygon(verts, closed=True,
                              facecolor=self.color, edgecolor="black", lw=2)
        ax.add_patch(polygon)

        # dimension annotations
        ax.annotate("", xy=(self.a / 2, -0.3), xytext=(-self.a / 2, -0.3),
                    arrowprops=dict(arrowstyle="<->", color="gray"))
        ax.text(0, -0.5, f"a = {self.a}", ha="center", fontsize=9, color="gray")

        ax.annotate("", xy=(self.b / 2, self.h + 0.3),
                    xytext=(-self.b / 2, self.h + 0.3),
                    arrowprops=dict(arrowstyle="<->", color="gray"))
        ax.text(0, self.h + 0.5, f"b = {self.b}", ha="center", fontsize=9, color="gray")

        ax.annotate("", xy=(self.a / 2 + 0.4, self.h),
                    xytext=(self.a / 2 + 0.4, 0),
                    arrowprops=dict(arrowstyle="<->", color="gray"))
        ax.text(self.a / 2 + 0.6, self.h / 2, f"h = {self.h}",
                va="center", fontsize=9, color="gray")

        # figure label
        ax.text(0, self.h / 2, label, ha="center", va="center",
                fontsize=11, fontweight="bold")

        # legend patch
        patch = mpatches.Patch(facecolor=self.color, edgecolor="black",
                               label=f"Area = {self.area():.2f}")
        ax.legend(handles=[patch], loc="upper right")

        margin = max(self.a, self.h) * 0.3
        ax.set_xlim(-self.a / 2 - margin, self.a / 2 + margin * 2)
        ax.set_ylim(-margin * 1.5, self.h + margin * 1.5)
        ax.set_aspect("equal")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_title(str(self))
        ax.grid(True, alpha=0.3)

        save_path = save_dir / "trapezoid.png"
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
        plt.show()
