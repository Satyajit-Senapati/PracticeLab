"""evaluate_reverse_polish_notation.py

Problem Statement:
Implement a Python module that evaluates the value of an arithmetic expression in Reverse Polish Notation.

Interview Difficulty: Easy
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: stack evaluation, postfix notation, operator application,
expression parsing
Real-world Use Case: Evaluating postfix expressions in compilers and stack-based calculators.
Input Description: Function accepts a list of tokens representing a postfix expression.
Output Description: Returns the integer result of the expression.
Example Inputs and Outputs:
    tokens = ["2","1","+","3","*"] -> 9
Constraints: Use integer division truncating toward zero for / operator.
Brute Force Approach: Convert to infix and evaluate with eval.
Optimized Approach: Use stack-based evaluation of postfix tokens.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    push integers on stack, pop two values for operators, compute and push result.
Edge Cases: single token and negative results.
Common Mistakes: wrong operand order for subtraction/division.
Follow-up Interview Questions:
    1. How to convert infix to postfix?
    2. Can you support additional operators like ^?
    3. What if tokens include variables?
Alternative Approaches: Evaluate recursively on a token iterator.
Expected Output: The script prints the evaluated RPN results for sample expressions.
Key Takeaways: Postfix evaluation is straightforward with a stack.
"""

from __future__ import annotations

from typing import List


def eval_rpn(tokens: List[str]) -> int:
    stack: List[int] = []
    for token in tokens:
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[-1]


def main() -> None:
    print('[2,1,+,3,*] =', eval_rpn(['2', '1', '+', '3', '*']))
    print('[4,13,5,/,+] =', eval_rpn(['4', '13', '5', '/', '+']))


if __name__ == '__main__':
    main()
