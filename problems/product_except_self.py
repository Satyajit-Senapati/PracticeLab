"""product_except_self.py

Problem Statement:
Implement a Python module that computes the product of all elements except the
current one for each position in an array without using division.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: prefix/suffix products, array traversal, edge-case handling,
space optimization
Real-world Use Case: Feature engineering, geometric mean computations,
and data normalization where element-wise exclusion is needed.
Input Description: Functions accept a list of integers.
Output Description: Functions return a list of products for each index.
Example Inputs and Outputs:
    product_except_self([1, 2, 3, 4]) -> [24, 12, 8, 6]
Constraints: Use O(n) time, avoid division, and minimize extra space.
Brute Force Approach: Compute product for each index by multiplying all other
values.
Optimized Approach: Use prefix and suffix products.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    values = [1, 2, 3, 4]
    prefix = [1, 1, 2, 6]
    suffix = [24, 12, 4, 1]
    result = [24, 12, 8, 6]
Edge Cases: empty list, single-element list, zeros in the array, and negative
values.
Common Mistakes: using division, not handling zeros correctly, and overusing
nested loops.
Follow-up Interview Questions:
    1. How would you solve this in constant extra space?
    2. What if zeros are allowed in the array?
    3. Can you adapt this for floating-point values?
Alternative Approaches: Use division when input guarantees no zeros or apply
logarithms for floating-point arrays.
Expected Output: The script prints product arrays for sample inputs.
Key Takeaways: Combine prefix and suffix accumulations to compute exclusionary
product values efficiently.
"""

from __future__ import annotations

from typing import List


def product_except_self(values: List[int]) -> List[int]:
    """Return product of all elements except self for each index."""
    length = len(values)
    if length == 0:
        return []

    prefix_products: List[int] = [1] * length
    suffix_products: List[int] = [1] * length

    for i in range(1, length):
        prefix_products[i] = prefix_products[i - 1] * values[i - 1]

    for i in range(length - 2, -1, -1):
        suffix_products[i] = suffix_products[i + 1] * values[i + 1]

    return [prefix_products[i] * suffix_products[i] for i in range(length)]


def main() -> None:
    """Main function demonstrating product except self."""
    examples = [
        [1, 2, 3, 4],
        [0, 1, 2, 3],
        [2, 0, 2, 3],
    ]
    for values in examples:
        print(values, "->", product_except_self(values))


if __name__ == "__main__":
    main()
