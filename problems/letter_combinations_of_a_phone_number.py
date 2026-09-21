"""letter_combinations_of_a_phone_number.py

Problem Statement:
Implement a Python module that returns all possible letter combinations a digit string could represent.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: backtracking, recursion, combinatorial generation,
phone keypad mapping
Real-world Use Case: Generating predictive text candidates from numeric input.
Input Description: Function accepts a string of digits 2-9.
Output Description: Returns all possible letter combinations.
Example Inputs and Outputs:
    digits = "23" -> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Constraints: digits '0' and '1' do not map to letters.
Brute Force Approach: Nested loops for each digit.
Optimized Approach: Use DFS/backtracking to build combinations.
Time Complexity: O(3^n * 4^m)
Space Complexity: O(n)
Step-by-step Dry Run:
    recursively append letters for each digit and add complete combinations.
Edge Cases: empty input returns empty list.
Common Mistakes: treating 0 or 1 as valid mappings.
Follow-up Interview Questions:
    1. Can you return combinations in lexicographic order?
    2. How does this scale for longer digit strings?
    3. What if digits can repeat?
Alternative Approaches: Use iterative product construction.
Expected Output: The script prints all letter combos for sample digits.
Key Takeaways: Backtracking cleanly generates all combinations from digit mappings.
"""
