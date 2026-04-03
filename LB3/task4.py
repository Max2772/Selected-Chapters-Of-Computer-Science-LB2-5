"""
Task 4: Analyse a predefined sentence (words separated by spaces and commas).
        Variant 3:
          a) count words; print all words whose letter count is even;
          b) find the shortest word that starts with 'a';
          c) print all repeated words.
        No regular expressions are used.

Subject: IGI
Lab Work: 3
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 27.03.2025
"""

TEXT = (
    "So she was considering in her own mind, as well as she could, for the "
    "hot day made her feel very sleepy and stupid, whether the pleasure of "
    "making a daisy-chain would be worth the trouble of getting up and "
    "picking the daisies, when suddenly a White Rabbit with pink eyes ran "
    "close by her."
)


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def tokenize(text: str) -> list[str]:
    """
    Split text into lowercase words, stripping all non-alphabetic characters
    (punctuation, hyphens, etc.) from each token.
    Words separated by spaces or commas are both handled.
    No regular expressions are used.

    Args:
        text (str): raw input sentence

    Returns:
        list[str]: list of clean lowercase words (empty tokens discarded)
    """
    words = []
    for raw in text.replace(",", " ").split():
        clean = "".join(c for c in raw if c.isalpha())
        if clean:
            words.append(clean.lower())
    return words


def words_with_even_letter_count(words: list[str]) -> list[str]:
    """
    Return words whose length (number of letters) is even.

    Args:
        words (list[str]): list of words

    Returns:
        list[str]: filtered list
    """
    return [w for w in words if len(w) % 2 == 0]


def shortest_word_starting_with(words: list[str], letter: str) -> str | None:
    """
    Find the shortest word that starts with letter (case-insensitive).

    Args:
        words  (list[str]): list of lowercase words
        letter (str)      : single character to match

    Returns:
        str | None: the shortest matching word, or None if none found
    """
    candidates = [w for w in words if w.startswith(letter.lower())]
    if not candidates:
        return None
    return min(candidates, key=len)


def repeated_words(words: list[str]) -> list[str]:
    """
    Return words that appear more than once in words, preserving first-seen
    order and without duplicates in the result.

    Args:
        words (list[str]): list of lowercase words

    Returns:
        list[str]: words that occur at least twice
    """
    seen = {}
    for w in words:
        seen[w] = seen.get(w, 0) + 1
    # Preserve order of first appearance
    added = set()
    result = []
    for w in words:
        if seen[w] > 1 and w not in added:
            result.append(w)
            added.add(w)
    return result


# ---------------------------------------------------------------------------
# Task entry point
# ---------------------------------------------------------------------------

def run():
    """
    Entry point for Task 4.

    Analyses the predefined TEXT string and prints:
      a) total word count and all words with an even letter count;
      b) the shortest word starting with 'a';
      c) all words that appear more than once.
    """
    words = tokenize(TEXT)

    # --- a) ---
    even_words = words_with_even_letter_count(words)
    print(f"Word count: {len(words)}")
    print(f"Words with even letter count: {len(even_words)}")
    for i, w in enumerate(even_words):
        print(f"\t{i + 1}) {w} (length: {len(w)})")

    # --- b) ---
    letter = "a"
    shortest_a = shortest_word_starting_with(words, letter)
    if shortest_a:
        print(f"Shortest word starting with '{letter}': {shortest_a}")
    else:
        print(f"No word starting with '{letter}' found.")

    # --- c) ---
    repeats = repeated_words(words)
    if repeats:
        print(f"Repeated words: {len(repeats)}")
        for i, w in enumerate(repeats):
            print(f"\t{i+1}) {w}")
    else:
        print("No repeated words found.")
