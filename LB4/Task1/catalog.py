"""
Catalog classes for Task1.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

import csv
import pickle
from abc import abstractmethod, ABC
from pathlib import Path

from LB4.Task1.book import Book
from LB4.Task1.mixins import PrintMixin


class CatalogBase(ABC):
    """Abstract base for catalog storage."""

    @abstractmethod
    def save(self, books: list, filename: str):
        """Save books to file."""

    @abstractmethod
    def load(self, filename: str) -> list:
        """Load books from file."""


class CSVCatalog(PrintMixin, CatalogBase):
    """CSV-backed catalog with built-in display (mixin)."""
    def __init__(self, directory: Path):
        self.directory = directory

    def save(self, books: list, filename: str):
        """Write books to a CSV file."""
        path = self.directory / filename
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["Title", "Author", "Year"])
            for b in books:
                w.writerow([b._title, b._author, b.year])

    def load(self, filename: str) -> list:
        """Read books from a CSV file."""
        path = self.directory / filename
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        with open(path, encoding="utf-8") as f:
            return [Book(r["Title"], r["Author"], int(r["Year"]))
                    for r in csv.DictReader(f)]


class PickleCatalog(PrintMixin, CatalogBase):
    """Pickle-backed catalog with built-in display (mixin)."""
    def __init__(self, directory: Path):
        self.directory = directory

    def save(self, books: list, filename: str):
        """Serialise books to a pickle file."""
        path = self.directory / filename
        with open(path, "wb") as f:
            pickle.dump(books, f)

    def load(self, filename: str) -> list:
        """Deserialise books from a pickle file."""
        path = self.directory / filename
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        with open(path, "rb") as f:
            return pickle.load(f)
