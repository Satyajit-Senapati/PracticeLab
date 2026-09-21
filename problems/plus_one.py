"""plus_one.py

Problem Statement:
Add one to a number represented as a list of digits.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Google, Microsoft
Concepts Tested: array manipulation, carry propagation.
Real-world Use Case: arbitrary precision arithmetic and digit-based addition.
Input Description: A list of digits representing a non-negative integer.
Output Description: The digits list after adding one.
Example Inputs and Outputs:
    [1,2,3] -> [1,2,4]
    [9,9] -> [1,0,0]
Constraints: Handle carry across multiple digits.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def plus_one(digits: list[int]) -> list[int]:
    """Add one to the represented integer and return the resulting digits."""
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


def main() -> None:
    examples = [
        [1, 2, 3],
        [4, 3, 2, 1],
        [9],
        [9, 9, 9],
    ]
    for digits in examples:
        print(f"{digits} -> {plus_one(digits.copy())}")


if __name__ == "__main__":
    main()
