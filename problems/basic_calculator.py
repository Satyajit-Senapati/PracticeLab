"""basic_calculator.py

Problem Statement:
Implement a Python module that evaluates a simple arithmetic expression string.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: stack usage, expression parsing, operator precedence,
shunting-yard
Real-world Use Case: Implementing simple calculators, parsing user-entered formulas, and expression evaluation.
Input Description: Function accepts a string containing non-negative integers and +, -, *, / operators.
Output Description: Returns the evaluated integer result.
Example Inputs and Outputs:
    s = "3+2*2" -> 7
Constraints: Use integer division truncating toward zero.
Brute Force Approach: Recursively evaluate using built-in eval (not allowed).
Optimized Approach: Use a stack to apply multiplication and division immediately.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    parse numbers and operators, push values on stack, apply * and / when seen.
Edge Cases: spaces in input and single number expression.
Common Mistakes: incorrect operator precedence and division rounding.
Follow-up Interview Questions:
    1. Can you add parentheses support?
    2. What changes for negative numbers?
    3. How to handle floating-point operations?
Alternative Approaches: Convert to postfix notation then evaluate.
Expected Output: The script prints evaluation results for sample expressions.
Key Takeaways: A stack-based parser handles precedence without recursion.
"""

from __future__ import annotations

from typing import List


def calculate(s: str) -> int:
    """Evaluate a basic arithmetic expression with +, -, *, /."""
    stack: List[int] = []
    num = 0
    sign = '+'
    s = s.replace(' ', '')

    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        if ch in '+-*/' or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                top = stack.pop()
                stack.append(int(top / num))
            sign = ch
            num = 0

    return sum(stack)


def main() -> None:
    print('3+2*2 =', calculate('3+2*2'))
    print(' 3/2 ', calculate(' 3/2 '))
    print(' 3+5 / 2 ', calculate(' 3+5 / 2 '))


if __name__ == '__main__':
    main()
