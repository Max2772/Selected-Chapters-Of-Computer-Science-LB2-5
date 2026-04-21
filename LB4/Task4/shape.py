"""
Shape model for drawing shapes with area calculation in Task4.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class for geometric shapes with area calculation."""

    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the figure."""
        pass
