"""word_pattern.py

Problem Statement:
Implement a Python module that checks if a pattern matches a string of words
bijectively.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: hash map mapping, bijective relationships, string parsing,
pattern matching
Real-world Use Case: Template validation, structured input parsing, and
matching formats to data.
Input Description: Functions accept a pattern string and a space-separated
word string.
Output Description: Functions return True if the pattern matches bijectively,
otherwise False.
Example Inputs and Outputs:
    word_pattern("abba", "dog cat cat dog") -> True
    word_pattern("abba", "dog cat cat fish") -> False
Constraints: Ensure a one-to-one correspondence between pattern characters
and words.
Brute Force Approach: Compare every pattern character with each word.
Optimized Approach: Use dictionaries to map characters to words and vice
versa.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    pattern = "abba", s = "dog cat cat dog"
    return True
Edge Cases: pattern and word count mismatch, duplicate mappings, and empty
inputs.
Common Mistakes: one-to-many mappings, forgetting reverse map checks, and
ignoring extra words.
Follow-up Interview Questions:
    1. How would you handle patterns with repeated words?
    2. Can this be adapted for regex-like patterns?
    3. What if words can contain whitespace?
Alternative Approaches: Use two lists of indices to compare first occurrences.
Expected Output: The script prints pattern matching results for sample inputs.
Key Takeaways: Maintain bidirectional mappings to enforce bijective pattern matching.
"""
