"""basic_calculator_ii.py

Problem Statement:
Implement a Python module that evaluates a string expression containing +, -, parentheses, and integers.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: stack, parentheses handling, expression parsing,
operator precedence
Real-world Use Case: Parsing calculator input, evaluating nested expression strings, and formula processing.
Input Description: Function accepts a string containing integers, +, -, parentheses, and spaces.
Output Description: Returns the evaluated integer result.
Example Inputs and Outputs:
    s = "(1+(4+5+2)-3)+(6+8)" -> 23
Constraints: Assume valid input with no multiplication or division.
Brute Force Approach: Use eval on the input after sanitization.
Optimized Approach: Use two stacks for values and operators or a single stack with sign state.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    parse numbers, push sign state, evaluate when parentheses close.
Edge Cases: leading negative signs and nested parentheses.
Common Mistakes: mishandling sign after '(' and using incorrect precedence.
Follow-up Interview Questions:
    1. How to add * and / while preserving order?
    2. Can you evaluate without stacks?
    3. How would you support variables?
Alternative Approaches: Use recursive descent parsing.
Expected Output: The script prints evaluation results for sample expressions.
Key Takeaways: Parentheses can be handled by saving and restoring evaluation context.
"""

from __future__ import annotations

from typing import List


def calculate(s: str) -> int:
    """Evaluate a basic arithmetic expression with +, -, and parentheses."""
    stack: List[int] = [1]
    sign = 1
    result = 0
    num = 0

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch in '+-':
            result += sign * num
            num = 0
            sign = stack[-1] * (1 if ch == '+' else -1)
        elif ch == '(':
            stack.append(sign)
        elif ch == ')':
            result += sign * num
            num = 0
            stack.pop()

    result += sign * num
    return result


def main() -> None:
    print('(1+(4+5+2)-3)+(6+8) =', calculate('(1+(4+5+2)-3)+(6+8)'))
    print('2-(1+1) =', calculate('2-(1+1)'))


if __name__ == '__main__':
    main()
