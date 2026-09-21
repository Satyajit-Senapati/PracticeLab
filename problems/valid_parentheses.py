"""valid_parentheses.py

Problem Statement:
Implement a Python module that validates whether parentheses in a string are
balanced and properly nested.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: stacks, string parsing, matching pairs, edge-case handling
Real-world Use Case: Expression validation, syntax checking, and compiler
front-end parsing.
Input Description: Functions accept a string containing parentheses characters.
Output Description: Functions return True if the string is valid, otherwise
False.
Example Inputs and Outputs:
    is_valid("()") -> True
    is_valid("()[]{}") -> True
    is_valid("(]") -> False
Constraints: Use O(n) time and O(n) space for stack-based validation.
Brute Force Approach: Recursively validate each substring.
Optimized Approach: Use a stack and direct matching.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    s = "([{}])"
    return True
Edge Cases: empty string, odd-length strings, and unmatched closing
parentheses.
Common Mistakes: forgetting to check stack emptiness, mismatched types, and
using incorrect bracket pairs.
Follow-up Interview Questions:
    1. What is the stack invariant in this algorithm?
    2. How would you support additional bracket types?
    3. Can you do this without extra space?
Alternative Approaches: Use recursion or iterative index matching.
Expected Output: The script prints validation results for sample strings.
Key Takeaways: A stack is the natural data structure for matching nested
structures.
"""

from __future__ import annotations

from typing import Dict


def is_valid(s: str) -> bool:
    """Return True if the input string has valid parentheses nesting."""
    mapping: Dict[str, str] = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []

    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)

    return not stack


def main() -> None:
    """Main function demonstrating parentheses validation."""
    examples = [
        "()",
        "()[]{}",
        "(]",
        "([{}])",
        "([)]",
    ]
    for example in examples:
        print(example, "->", is_valid(example))


if __name__ == "__main__":
    main()
