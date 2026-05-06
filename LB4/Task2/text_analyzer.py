"""
Class for analysing text in Task2.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

import re
from abc import abstractmethod, ABC
from collections import defaultdict


class AnalyzerBase(ABC):
    """Abstract base for text analyzers."""

    @abstractmethod
    def find_emails(self) -> list:
        pass

    @abstractmethod
    def count_smileys(self) -> int:
        pass


class TextAnalyzer(AnalyzerBase):
    """Analyses text using regular expressions."""

    def __init__(self, text: str):
        self.text = text

    def find_emails(self) -> list[tuple[str, str]]:
        """
        Find all name–email pairs like 'Name <email>' or 'Name: email'.

        Returns: List of (name, email) tuples.
        """
        pattern = r'([A-Za-z][A-Za-z\s]+?)\s*[:<]\s*([\w.+-]+@[\w.-]+\.\w{2,4})>?'
        return re.findall(pattern, self.text)

    def replace_variable(self) -> str:
        """
        Replace $v_(i)$ (i = single digit or letter) with v[i].

        Example: '123$v_(ac)$bf$v_(1)$' -> '123$v_(ac)$bfv[1]'

        Returns: Modified string.
        """
        return re.sub(r'\$v_\(([A-Za-z0-9])\)\$', r'v[\1]', self.text)

    def odd_letter_words(self) -> tuple[int, list[str]]:
        """
        Count all words and collect those with an odd number of letters.

        Returns: (total_word_count, list_of_odd_words)
        """
        words = re.findall(r'\b[A-Za-z]+\b', self.text)
        odd = [w for w in words if len(w) % 2 != 0]
        return len(words), odd

    def shortest_i_word(self) -> str | None:
        """
        Find the shortest word starting with the letter 'i' (case-insensitive).

        Returns: The shortest such word, or None if none found.
        """
        words = re.findall(r'\b[iI][A-Za-z]*\b', self.text)
        return min(words, key=len) if words else None

    def repeated_words(self) -> list[str]:
        """
        Find all words that appear more than once (case-insensitive).

        Returns: Sorted list of repeated words in lowercase.
        """
        words = re.findall(r'\b[A-Za-z]+\b', self.text.lower())
        d = defaultdict(int)
        for w in words:
            d[w] += 1
        duplicates = [word for word in d if d[word] > 1]
        return sorted(duplicates)

    def sentence_stats(self) -> dict:
        """
        Compute sentence-level statistics.

        Returns: Dict with total, declarative, interrogative, exclamatory,
                 avg_sentence_len (words), avg_word_len (chars).
        """
        parts = re.split(r'([.!?])', self.text)
        sentences = []
        for i in range(0, len(parts) - 1, 2):
            s = (parts[i] + parts[i + 1]).strip()
            if s:
                sentences.append(s)

        words_all = re.findall(r'\b\w+\b', self.text)
        return {
            'total': len(sentences),
            'declarative': sum(1 for s in sentences if s.endswith('.')),
            'interrogative': sum(1 for s in sentences if s.endswith('?')),
            'exclamatory': sum(1 for s in sentences if s.endswith('!')),
            'avg_sentence_len': (len(words_all) / len(sentences) if sentences else 0),
            'avg_word_len': (
                sum(len(w) for w in words_all) / len(words_all)
                if words_all else 0
            ),
        }

    def count_smileys(self) -> int:
        """
        Count smileys: [:;]-*[()[]]+  with no other characters inside,
        not surrounded by non-whitespace.

        Returns: Number of smileys found.
        """
        pattern = r'(?<!\S)[:;]-*([()[\]])\1*(?!\S)'
        return len(re.findall(pattern, self.text))

    def __str__(self) -> str:
        return f"TextAnalyzer({len(self.text)} chars)"
