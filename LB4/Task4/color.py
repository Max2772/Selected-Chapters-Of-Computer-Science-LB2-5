"""
Color model for drawing shapes in Task4.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

import matplotlib.colors as mcolors


class Color:
    """Class to manage the color of a figure."""

    def __init__(self, color: str):
        self.color = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str):

        if not isinstance(value, str) or not value.strip():
            raise ValueError("Color must be a non-empty string.")

        if not mcolors.is_color_like(value):
            raise ValueError(f"Invalid color: '{value}'")

        self._color = value

    def __str__(self):
        return f"Shape color:{self._color}"
