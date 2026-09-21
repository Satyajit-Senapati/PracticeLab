"""decode_ways.py

Problem Statement:
Implement a Python module that counts the number of ways to decode a digit string.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: dynamic programming, recursion with memoization, string parsing,
combinatorics
Real-world Use Case: Translating encoded numeric messages into letter sequences.
Input Description: Function accepts a non-empty string containing digits.
Output Description: Returns the number of valid decodings.
Example Inputs and Outputs:
    s = "12" -> 2
    s = "226" -> 3
Constraints: '1' to '26' map to letters A-Z, and '0' must be part of valid two-digit numbers.
Brute Force Approach: Recursively explore all split points.
Optimized Approach: Use DP to count decodings for prefixes.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    dp[i] counts decodings for prefix length i, update based on one- and two-digit validity.
Edge Cases: leading zero and invalid two-digit codes.
Common Mistakes: treating '0' as valid alone and miscounting two-digit boundaries.
Follow-up Interview Questions:
    1. How to recover the actual decoding strings?
    2. Can you do this in O(1) space?
    3. What if the mapping is extended beyond 26?
Alternative Approaches: Use recursion with memoization.
Expected Output: The script prints decode counts for sample strings.
Key Takeaways: DP over prefixes handles valid numeric decode combinations efficiently.
"""
