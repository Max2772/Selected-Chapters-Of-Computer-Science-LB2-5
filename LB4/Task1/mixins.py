"""
Mixin class for Task1.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""


class PrintMixin:
    """Mixin that adds a formatted display method."""

    def show(self, books: list, heading: str = "Results"):
        """Print a labelled list of books."""
        print(f"\n{heading}:")
        if not books:
            print("    (no books found)")
        for i, b in enumerate(books, 1):
            print(f"\t{i}. {b}")
