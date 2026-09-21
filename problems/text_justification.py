"""text_justification.py

Problem Statement:
Implement a Python module that formats text into fully justified lines of a
specified width.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: string formatting, greedy algorithms, text processing,
edge-case handling, justification logic
Real-world Use Case: Generating console reports, fixed-width text output,
formatting email templates, and creating readable text layouts.
Input Description: Functions accept a list of words and a target line width.
Output Description: Functions return a list of justified lines of text.
Example Inputs and Outputs:
    justify_text(["This", "is", "an", "example"], 16) -> ["This    is    an", "example         "]
Constraints: Distribute spaces evenly between words, handle last line
left-justified, and manage single-word lines correctly.
Brute Force Approach: Build lines with minimal validation and spacing.
Optimized Approach: Use greedy accumulation and space distribution.
Time Complexity: O(n) for processing all words.
Space Complexity: O(n) for the output lines.
Step-by-step Dry Run:
    words = ["This", "is", "text"]
    width = 10
    return ["This    is", "text      "]
Edge Cases: single-word lines, last line left-justified, exact width lines,
and empty word lists.
Common Mistakes: distributing spaces incorrectly, ignoring the last line
rule, and miscalculating remaining spaces.
Follow-up Interview Questions:
    1. How does the greedy approach work here?
    2. How would you support right justification?
    3. Can you adapt this for proportional fonts?
Alternative Approaches: Use textwrap for simpler formatting, or custom
builders for fixed-width output.
Expected Output: The script prints justified text lines for sample input.
Key Takeaways: Implement greedy line accumulation and even space
distribution for text justification.
"""

from __future__ import annotations

from typing import List


def justify_line(words: List[str], max_width: int, is_last_line: bool) -> str:
    """Justify a single line of words to the given width."""
    if len(words) == 1 or is_last_line:
        return " ".join(words).ljust(max_width)

    total_word_length = sum(len(word) for word in words)
    total_spaces = max_width - total_word_length
    gaps = len(words) - 1
    even_space, extra_spaces = divmod(total_spaces, gaps)

    justified_words: List[str] = []
    for index, word in enumerate(words):
        justified_words.append(word)
        if index < gaps:
            spaces = even_space + (1 if index < extra_spaces else 0)
            justified_words.append(" " * spaces)

    return "".join(justified_words)


def justify_text(words: List[str], max_width: int) -> List[str]:
    """Justify the given words into lines of the specified width."""
    lines: List[str] = []
    current_line: List[str] = []
    current_length = 0

    for word in words:
        if current_length + len(current_line) + len(word) > max_width:
            lines.append(justify_line(current_line, max_width, is_last_line=False))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word)

    if current_line:
        lines.append(justify_line(current_line, max_width, is_last_line=True))

    return lines


def main() -> None:
    """Main function demonstrating text justification."""
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    justified = justify_text(words, 16)

    for line in justified:
        print(f"'{line}'")


if __name__ == "__main__":
    main()
