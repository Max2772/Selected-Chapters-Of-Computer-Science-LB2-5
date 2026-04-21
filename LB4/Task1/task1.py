"""
Task 1: Library book catalog.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

import pickle
from pathlib import Path

from LB4.Task1.catalog import CSVCatalog, PickleCatalog
from LB4.Task1.book import Book
from LB4.ui import read_str, read_int

BOOKS = [
    Book("The Master and Margarita", "Bulgakov", 1967),
    Book("White Guard", "Bulgakov", 1925),
    Book("Crime and Punishment", "Dostoevsky", 1866),
    Book("The Idiot", "Dostoevsky", 1869),
    Book("War and Peace", "Tolstoy", 1869),
    Book("Anna Karenina", "Tolstoy", 1878),
    Book("Eugene Onegin", "Pushkin", 1833),
    Book("Fathers and Sons", "Turgenev", 1862),
]


def choose_format(directory: Path) -> tuple:
    """Ask the user to pick CSV or Pickle."""

    while True:
        choice = read_int("\nChoose format (1 – CSV\t2 – Pickle): ")
        if choice == 1:
            return CSVCatalog(directory), "library.csv"
        if choice == 2:
            return PickleCatalog(directory), "library.pkl"
        else:
            print("Invalid choice")


def run():
    """Run the library catalog task."""
    script_dir = Path(__file__).parent

    catalog, path = choose_format(script_dir)

    try:
        catalog.save(BOOKS, path)
        books = catalog.load(path)
    except (OSError, ValueError, pickle.UnpicklingError) as e:
        print(f"Error: {e}")
        return

    print(f"Loaded {len(books)} books from '{path}'.")

    while True:
        query = read_str("Author last name (or 'quit' to exit): ").lower()
        if query == "quit":
            break

        found = sorted(
            b for b in books
            if query in b.author.lower()
        )
        catalog.show(found, heading=f'Books by "{query}"')
