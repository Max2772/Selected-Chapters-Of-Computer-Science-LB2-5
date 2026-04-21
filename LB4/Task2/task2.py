"""
Task 2: Text analysis using regular expressions.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

from pathlib import Path

from LB4.Task2.file_manager import FileManager
from LB4.Task2.text_analyzer import TextAnalyzer


def _build_report(analyzer: TextAnalyzer) -> str:
    """
    Assemble a full analysis report string.

    Args: analyzer: Populated TextAnalyzer instance.

    Returns: Multi-line report text.
    """
    report = ["=" * 52, "  ANALYSIS REPORT", "=" * 52]

    # emails
    emails = analyzer.find_emails()
    report.append("\n[Emails found]")
    if emails:
        for name, addr in emails:
            report.append(f"{name.strip()} - {addr}")
    else:
        report.append("(none found)")

    # variable replacement
    report.append("\n[Variable replacement  $v_(i)$ -> v[i]]")
    report.append(f"{analyzer.replace_variable()}")

    # odd-letter words
    total, odd = analyzer.odd_letter_words()
    report.append(f"\n[Words: {total} total]  Odd-letter words:")
    report.append((", ".join(odd) if odd else "(none)"))

    # shortest 'i' word
    iword = analyzer.shortest_i_word()
    report.append("\n[Shortest word starting with 'i']")
    report.append(f"{iword if iword else '(none found)'}")

    # repeated words
    reps = analyzer.repeated_words()
    report.append("\n[Repeated words]")
    report.append((", ".join(reps) if reps else "(none)"))

    # sentence stats
    st = analyzer.sentence_stats()
    report.append("\n[Sentence statistics]")
    report.append(f"Total:         {st['total']}")
    report.append(f"Declarative:   {st['declarative']}")
    report.append(f"Interrogative: {st['interrogative']}")
    report.append(f"Exclamatory:   {st['exclamatory']}")
    report.append(f"Avg sentence:  {st['avg_sentence_len']:.2f} words")
    report.append(f"Avg word len:  {st['avg_word_len']:.2f} chars")

    # smileys
    report.append(f"\n[Smileys found: {analyzer.count_smileys()}]")
    report.append("=" * 52)

    return "\n".join(report)


def run():
    """Run the text analysis task."""
    script_dir = Path(__file__).parent
    fm = FileManager(script_dir)

    try:
        text = fm.read("text.txt")
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print("Please create 'text.txt' in the LB4/Task2 folder.")
        return

    analyzer = TextAnalyzer(text)
    report = _build_report(analyzer)

    print(report)

    try:
        fm.write("output.txt", report)
        info = fm.zip_file("output.txt", "results.zip")
        print(f"\nSaved to output.txt and archived to results.zip")
        print(f"Archive info: {info['name']}, {info['size']} B -> {info['compress_size']} B")
    except OSError as e:
        print(f"\nError saving results: {e}")