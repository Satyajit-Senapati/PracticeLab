"""word_pattern_ii.py

Problem Statement:
Implement a Python module that determines if a string follows a given pattern with bijection.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: hashing, bijective mapping, pattern matching, string tokenization
Real-world Use Case: Mapping structured templates to input tokens and validating format constraints.
Input Description: Function accepts a pattern string and a corresponding string of words.
Output Description: Returns True if the words follow the pattern, otherwise False.
Example Inputs and Outputs:
    pattern = "abba", s = "dog cat cat dog" -> True
    pattern = "abba", s = "dog cat cat fish" -> False
Constraints: Each pattern character maps to exactly one word, and words map to exactly one character.
Brute Force Approach: Try all possible bijections.
Optimized Approach: Use two dictionaries for forward and reverse mapping.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    split s into words and compare mapping for each character-word pair.
Edge Cases: unequal lengths and repeated pattern letters mapping to different words.
Common Mistakes: allowing non-bijective mappings or ignoring word boundaries.
Follow-up Interview Questions:
    1. How to handle patterns with wildcards?
    2. Can you generalize to arbitrary token patterns?
    3. What if the pattern uses digits or multicharacter tokens?
Alternative Approaches: Use a single map with canonical indices.
Expected Output: The script prints pattern validation results for sample inputs.
Key Takeaways: Bidirectional mapping ensures one-to-one correspondence.
"""
