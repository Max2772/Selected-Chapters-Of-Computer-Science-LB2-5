"""
Calculator model for series expansion in Task3.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

import math
from collections import defaultdict
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt


class SeriesCalculator:
    """
    Calculates ln(1+x) via power series and computes sequence statistics.
    """

    MAX_ITER = 500

    def __init__(self, x: float, eps: float):
        self._terms: list[float] = []
        self.x = x
        self.eps = eps

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        if not (-1 < value <= 1):
            raise ValueError("x must be in (-1, 1].")
        self._x = value

    @property
    def eps(self) -> float:
        return self._eps

    @eps.setter
    def eps(self, value: float):
        if value <= 0:
            raise ValueError("eps must be positive.")
        self._eps = value

    def _term_generator(self):
        """Yield successive terms of the ln(1+x) series."""
        n = 1
        while True:
            yield ((-1) ** (n + 1)) * (self._x ** n) / n
            n += 1

    def calculate(self) -> tuple[float, int]:
        """
        Sum the series until |term| < eps.

        Returns: (approximated value, number of terms used)
        Raises: ValueError: If convergence is not reached.
        """
        self._terms.clear()
        total = 0.0
        for n, term in enumerate(self._term_generator(), 1):
            self._terms.append(term)
            total += term
            if abs(term) < self._eps:
                return total, n
            if n >= self.MAX_ITER:
                raise ValueError(f"Did not converge in {self.MAX_ITER} iterations.")
        return total, len(self._terms)

    def statistics(self) -> dict:
        """
        Compute mean, median, mode, variance and std of accumulated terms.

        Raises: ValueError: If calculate() hasn't been called yet.
        """
        data = self._terms
        if not data:
            raise ValueError("No terms, call calculate() first.")

        n = len(data)
        mean = sum(data) / n
        s = sorted(data)
        median = (s[n // 2 - 1] + s[n // 2]) / 2 if n % 2 == 0 else s[n // 2]

        freq = defaultdict(int)
        for v in data:
            freq[v] += 1
        max_f = max(freq.values())
        mode = [k for k, v in freq.items() if v == max_f]

        variance = sum((v - mean) ** 2 for v in data) / n
        return dict(mean=mean, median=median, mode=mode, variance=variance, std=math.sqrt(variance))

    def plot(self, approx: float, save_dir: Path):
        """Draw series vs exact function and save to plot.png."""
        xs = np.linspace(-0.99, 1.0, 200)
        n = len(self._terms)
        y_exact = [math.log(1 + v) for v in xs]
        y_series = [
            sum(((-1) ** (k + 1)) * (v ** k) / k for k in range(1, n + 1))
            for v in xs
        ]

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(xs, y_exact, color="blue", label="math.log(1+x) — exact")
        ax.plot(xs, y_series, color="red", linestyle="--", label=f"Series ({n} terms)")
        ax.scatter(self._x, approx, color="green", zorder=5,
                   label=f"Point (x={self._x:.3f})")
        ax.annotate(
            f"x={self._x:.6f}\nF(x)≈{approx:.6f}\neps={self._eps:e}",
            xy=(self._x, approx), xytext=(20, -30),
            textcoords="offset points",
            arrowprops=dict(arrowstyle="->", color="black"),
            fontsize=9
        )
        ax.axhline(0, color="black", linewidth=0.6)
        ax.axvline(0, color="black", linewidth=0.6)
        ax.set_title("ln(1+x) — Series expansion vs exact value")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        ax.grid(True, linestyle=":", alpha=0.7)

        path = save_dir / "plot.png"
        fig.savefig(path)
        print(f"\nPlot saved: {path}")
        plt.show()

    def __str__(self) -> str:
        return f"SeriesCalculator(x={self._x}, eps={self._eps})"
