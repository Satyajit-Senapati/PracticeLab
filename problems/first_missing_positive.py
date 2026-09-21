"""first_missing_positive.py

Problem Statement:
Implement a Python module that returns the smallest missing positive integer from an unsorted list.

Interview Difficulty: Hard
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: in-place array manipulation, index mapping, O(n) time,
constant space
Real-world Use Case: Assigning smallest available identifiers and missing sequence detection.
Input Description: Function accepts a list of integers.
Output Description: Returns the smallest missing positive integer.
Example Inputs and Outputs:
    nums = [3,4,-1,1] -> 2
Constraints: Achieve O(n) time and O(1) extra space.
Brute Force Approach: Sort the array or use a hash set.
Optimized Approach: Place each number in its correct index position.
Time Complexity: O(n)
Space Complexity: O(1)
Step-by-step Dry Run:
    swap nums[i] to nums[nums[i]-1] until all valid positions are filled.
Edge Cases: empty list and array with consecutive positives.
Common Mistakes: not using while swap loops correctly or failing to skip invalid values.
Follow-up Interview Questions:
    1. Can you extend this to find the kth missing positive?
    2. How does this compare to using a hash set?
    3. What if duplicates are present?
Alternative Approaches: Use a set with O(n) time and O(n) space.
Expected Output: The script prints the smallest missing positive integer for sample input.
Key Takeaways: Index-based placement enables constant extra space solutions.
"""
