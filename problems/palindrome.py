"""palindrome.py

Problem Statement:
Implement a Python module that checks whether text is a palindrome, including
case normalization and optional punctuation removal.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: string normalization, palindrome logic, edge-case handling,
text processing
Real-world Use Case: Validating identifiers, checking symmetric text patterns,
content filtering, and building string-based validation utilities.
Input Description: Functions accept strings and optional normalization flags.
Output Description: Functions return boolean results indicating palindrome
status.
Example Inputs and Outputs:
    is_palindrome("madam") -> True
    is_palindrome("A man, a plan, a canal: Panama") -> True
    is_palindrome("hello") -> False
Constraints: Handle empty strings, normalize case, and optionally ignore
non-alphanumeric characters.
Brute Force Approach: Compare characters pairwise with manual index movement.
Optimized Approach: Normalize text and use slicing or two-pointer checks.
Time Complexity: O(n) for normalization and palindrome checks.
Space Complexity: O(n) for the normalized string.
Step-by-step Dry Run:
    value = "Madam"
    normalized = "madam"
    return True
Edge Cases: empty string, punctuation only, whitespace, and mixed case.
Common Mistakes: ignoring non-alphanumeric characters, using Python slices
incorrectly, and failing to normalize case.
Follow-up Interview Questions:
    1. How do you handle Unicode characters in palindrome checks?
    2. What is the benefit of a two-pointer approach here?
    3. Can this be done in-place with a character array?
Alternative Approaches: Use generator expressions, two-pointer iteration, or
stack-based reversal.
Expected Output: The script prints palindrome check results for sample inputs.
Key Takeaways: Normalize input before comparison and use concise, explicit
logic to determine palindrome status.
"""

from __future__ import annotations

import re


def normalize_text(text: str, ignore_non_alphanumeric: bool = True) -> str:
    """Normalize text for palindrome checking."""
    normalized = text.lower()
    if ignore_non_alphanumeric:
        normalized = re.sub(r"[^a-z0-9]", "", normalized)
    return normalized


def is_palindrome(text: str, ignore_non_alphanumeric: bool = True) -> bool:
    """Return True if the text is a palindrome after normalization."""
    normalized = normalize_text(text, ignore_non_alphanumeric)
    return normalized == normalized[::-1]


def is_palindrome_two_pointer(text: str, ignore_non_alphanumeric: bool = True) -> bool:
    """Check palindrome status using a two-pointer approach."""
    normalized = normalize_text(text, ignore_non_alphanumeric)
    left, right = 0, len(normalized) - 1
    while left < right:
        if normalized[left] != normalized[right]:
            return False
        left += 1
        right -= 1
    return True


def main() -> None:
    """Main function demonstrating palindrome checks."""
    examples = [
        "madam",
        "A man, a plan, a canal: Panama",
        "hello",
    ]
    for example in examples:
        print(example, "->", is_palindrome(example))
        print(example, "two-pointer ->", is_palindrome_two_pointer(example))


if __name__ == "__main__":
    main()
