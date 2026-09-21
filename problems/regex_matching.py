"""regex_matching.py

Problem Statement:
Implement a Python module that demonstrates regular expression matching and
validation for common patterns like email, phone numbers, and log parsing.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: regular expressions, pattern matching, validation,
re module, named groups, search vs match
Real-world Use Case: Validating user inputs, parsing logs, extracting fields
from text, and filtering records in data processing.
Input Description: Functions accept strings and regular expression patterns.
Output Description: Functions return boolean validation results, extracted
fields, and matched values.
Example Inputs and Outputs:
    is_valid_email("user@example.com") -> True
    extract_phone_number("Call 555-1234") -> "555-1234"
    parse_log_line("INFO 2026-07-03 event") -> {...}
Constraints: Use Python `re` module idiomatically, compile patterns once,
handle missing matches gracefully, and avoid overly permissive regex.
Brute Force Approach: Use manual string scanning and splitting.
Optimized Approach: Use compiled regex patterns and named capture groups.
Time Complexity: O(n) per match operation.
Space Complexity: O(n) for matched strings and groups.
Step-by-step Dry Run:
    is_valid_email("user@example.com") -> True
    return True
Edge Cases: invalid formats, missing fields, empty input, and overlapping
patterns.
Common Mistakes: using greedy quantifiers incorrectly, ignoring anchors, and
not escaping special characters.
Follow-up Interview Questions:
    1. When should you use regex over plain string methods?
    2. What is the difference between `match()` and `search()`?
    3. How do named groups improve readability?
Alternative Approaches: Use parsing libraries, tokenizer-based validation,
or simple string split logic when patterns are trivial.
Expected Output: The script prints validation and parsing results for sample
inputs.
Key Takeaways: Use regex for structured text matching and keep patterns clear
and maintainable.
"""

from __future__ import annotations

import re
from typing import Dict, Optional


EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
PHONE_NUMBER = r"(?:(?:\+\d{1,3} )?(?:\(\d{3}\)|\d{3})[- .]?)?\d{3}[- .]?\d{4}"
PHONE_PATTERN = re.compile(PHONE_NUMBER)
PHONE_SEARCH_PATTERN = re.compile(r"(?<![\w+])" + PHONE_NUMBER + r"(?!\w)")
LOG_PATTERN = re.compile(
    r"^(?P<level>INFO|WARNING|ERROR|DEBUG)\s+(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<message>.+)$"
)


def is_valid_email(value: str) -> bool:
    """Validate whether a string is a well-formed email address."""
    return bool(EMAIL_PATTERN.fullmatch(value))


def is_valid_phone(value: str) -> bool:
    """Validate whether a string is a phone number."""
    return bool(PHONE_PATTERN.fullmatch(value))


def extract_phone_number(value: str) -> Optional[str]:
    """Extract a phone number from a text string if present."""
    match = PHONE_SEARCH_PATTERN.search(value)
    return match.group(0) if match else None


def parse_log_line(line: str) -> Optional[Dict[str, str]]:
    """Parse a structured log line with named capture groups."""
    match = LOG_PATTERN.match(line)
    if match:
        return match.groupdict()
    return None


def main() -> None:
    """Main function demonstrating regex matching examples."""
    examples = [
        "user@example.com",
        "invalid-email@",
    ]
    for example in examples:
        print(example, "valid email ->", is_valid_email(example))

    phone_examples = [
        "+1 (555) 123-4567",
        "555-1234",
    ]
    for example in phone_examples:
        print(example, "valid phone ->", is_valid_phone(example))
        print(example, "extracted phone ->", extract_phone_number(example))

    log_examples = [
        "INFO 2026-07-03 Event completed successfully",
        "ERROR 2026-07-03 Failure encountered",
    ]
    for log in log_examples:
        print(log, "parsed ->", parse_log_line(log))


if __name__ == "__main__":
    main()
