"""reverse_string.py

Problem Statement:
Implement a Python module that reverses strings using multiple approaches,
demonstrating slicing, iterative construction, and recursion.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: string manipulation, slicing, iteration, recursion,
edge-case handling, time complexity
Real-world Use Case: Reversing text for encoding, creating palindrome checks,
processing user input, and building utility functions for text transformation.
Input Description: Functions accept strings and optional boolean flags for
strategy selection.
Output Description: Functions return the reversed string and demonstrate
correct handling of empty and multi-character inputs.
Example Inputs and Outputs:
    reverse_string("hello") -> "olleh"
    reverse_string_recursive("abc") -> "cba"
    reverse_string_iterative("") -> ""
Constraints: Use clear function design, avoid modifying the input, and preserve
Unicode characters correctly.
Brute Force Approach: Iterate over the string and accumulate reversed characters.
Optimized Approach: Use Python slicing for concise and efficient reversal.
Time Complexity: O(n) for string reversal operations.
Space Complexity: O(n) for the returned reversed string.
Step-by-step Dry Run:
    value = "abc"
    reversed_value = "cba"
    return reversed_value
Edge Cases: empty strings, single-character strings, strings containing
Unicode characters, and whitespace preservation.
Common Mistakes: using in-place modification on immutable strings and ignoring
Unicode or multi-byte character behavior.
Follow-up Interview Questions:
    1. Why is string reversal O(n) in Python?
    2. How do slicing and recursion compare for this problem?
    3. Can you reverse a string in place in Python?
Alternative Approaches: Use `reversed()` with `join()`, recursion, or manual
loop accumulation.
Expected Output: The script prints examples of reversed strings using
multiple approaches.
Key Takeaways: Use slicing for simple string reversal, and choose alternatives
when explicit iteration or recursion is required.
"""

from __future__ import annotations

from typing import Callable


def reverse_string(text: str) -> str:
    """Reverse a string using slicing."""
    return text[::-1]


def reverse_string_iterative(text: str) -> str:
    """Reverse a string using an iterative loop."""
    reversed_chars = []
    for char in text:
        reversed_chars.insert(0, char)
    return "".join(reversed_chars)


def reverse_string_recursive(text: str) -> str:
    """Reverse a string recursively."""
    if len(text) <= 1:
        return text
    return reverse_string_recursive(text[1:]) + text[0]


def reverse_with_function(text: str, strategy: Callable[[str], str]) -> str:
    """Reverse a string using a provided reversal strategy."""
    return strategy(text)


def main() -> None:
    """Main function demonstrating string reversal approaches."""
    sample = "hello"
    slicing_result = reverse_string(sample)
    iterative_result = reverse_string_iterative(sample)
    recursive_result = reverse_string_recursive(sample)
    strategy_result = reverse_with_function(sample, reverse_string)

    print("Slicing reversal:", slicing_result)
    print("Iterative reversal:", iterative_result)
    print("Recursive reversal:", recursive_result)
    print("Strategy reversal:", strategy_result)


if __name__ == "__main__":
    main()
