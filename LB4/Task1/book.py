"""
Book class for Task1.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""


class Book:
    """A single library book with title, author and year."""

    def __init__(self, title: str, author: str, year: int):
        self._title = title
        self._author = author
        self._year = year

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int):
        value = int(value)
        if not (1 <= value <= 2026):
            raise ValueError("Year must be between 1 and 2026.")
        self._year = value

    def __str__(self) -> str:
        return f'"{self._title}"  —  {self._author}  ({self._year})'

    def __lt__(self, other: "Book") -> bool:
        """Sort books by year."""
        return self._year < other._year
