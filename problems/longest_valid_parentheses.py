"""longest_valid_parentheses.py

Problem Statement:
Implement a Python module that finds the length of the longest valid parentheses substring.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: stack, dynamic programming, string scanning,
balanced parentheses
Real-world Use Case: Validating nested expressions and computing longest balanced segments.
Input Description: Function accepts a string containing '(' and ')' characters.
Output Description: Returns the length of the longest valid parentheses substring.
Example Inputs and Outputs:
    s = "(()" -> 2
    s = ")()())" -> 4
Constraints: Use O(n) time.
Brute Force Approach: Check all substrings for validity.
Optimized Approach: Use a stack to track indices of unmatched parentheses.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    push indices of unmatched opens and last invalid position, compute distances for valid segments.
Edge Cases: all opens or all closes.
Common Mistakes: using the wrong base index after unmatched parentheses.
Follow-up Interview Questions:
    1. Can you solve it with DP?
    2. How to handle other bracket types?
    3. What is the maximum nesting depth?
Alternative Approaches: Use two-pass left-right scan.
Expected Output: The script prints longest valid parentheses lengths for sample inputs.
Key Takeaways: Tracking indices of unmatched parentheses gives valid substring lengths efficiently.
"""
