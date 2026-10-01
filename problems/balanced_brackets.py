"""balanced_brackets.py

Problem Statement:
Check whether brackets (), [], and {} are balanced and properly nested. Ignore non-bracket characters.
Interview Difficulty: Easy
Concepts Tested: stack, parsing, nesting
Input Description: A string containing brackets and other characters.
Output Description: A boolean.
Example Inputs and Outputs:
    balanced_brackets("a{b[c](d)}") -> True
Constraints: A string containing brackets and other characters.
Time Complexity: O(n)
Space Complexity: O(n)
"""


def balanced_brackets(text: str) -> bool:
    stack = []
    closing = {")": "(", "]": "[", "}": "{"}
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in closing:
            if not stack or stack.pop() != closing[char]:
                return False
    return not stack
