"""word_frequency.py

Problem Statement:
Implement a Python module that computes word frequency counts from a text
string, demonstrating normalization, tokenization, and frequency aggregation.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: text processing, tokenization, normalization, Counter,
frequency analysis, data aggregation
Real-world Use Case: Building search term analytics, summarizing document
content, detecting common keywords, and preprocessing text for NLP.
Input Description: Functions accept a string of text.
Output Description: Functions return frequency dictionaries and sorted
frequency lists.
Example Inputs and Outputs:
    word_frequency("Hello hello world") -> {'hello': 2, 'world': 1}
    top_n_words(..., 1) -> [('hello', 2)]
Constraints: Normalize text to lowercase, strip punctuation, and handle empty
inputs safely.
Brute Force Approach: Iterate over tokens and manually update counts.
Optimized Approach: Use `collections.Counter` for frequency aggregation.
Time Complexity: O(n) for tokenization and counting.
Space Complexity: O(k) for distinct words.
Step-by-step Dry Run:
    text = "Hello world hello"
    frequencies = {'hello': 2, 'world': 1}
    return frequencies
Edge Cases: empty string, punctuation-only input, case variations, and
repeated whitespace.
Common Mistakes: not normalizing case, splitting on punctuation incorrectly,
and ignoring empty tokens.
Follow-up Interview Questions:
    1. How would you handle stop words or stemming?
    2. Can you make this Unicode-aware?
    3. How do you optimize for large text streams?
Alternative Approaches: Use regular expressions for tokenization or NLP
libraries for advanced preprocessing.
Expected Output: The script prints frequency dictionaries and top word counts
for sample text.
Key Takeaways: Normalize and tokenize text cleanly before computing frequencies.
"""

from __future__ import annotations

import re
from collections import Counter
from typing import Dict, List, Tuple


def normalize_text(text: str) -> List[str]:
    """Normalize and tokenize text into words."""
    normalized = text.lower()
    tokens = re.findall(r"[a-z0-9]+", normalized)
    return tokens


def word_frequency(text: str) -> Dict[str, int]:
    """Return the frequency count of each word in the input text."""
    tokens = normalize_text(text)
    return dict(Counter(tokens))


def top_n_words(text: str, n: int) -> List[Tuple[str, int]]:
    """Return the top N most frequent words."""
    frequencies = word_frequency(text)
    return sorted(frequencies.items(), key=lambda item: item[1], reverse=True)[:n]


def main() -> None:
    """Main function demonstrating word frequency analysis."""
    text = "Hello, hello world! This is a test. Test this code."
    frequencies = word_frequency(text)
    top_words = top_n_words(text, 3)

    print("Word frequencies:", frequencies)
    print("Top words:", top_words)


if __name__ == "__main__":
    main()
