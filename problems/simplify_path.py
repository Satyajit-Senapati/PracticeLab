"""simplify_path.py

Problem Statement:
Implement a Python module that simplifies a Unix-style file path.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: stack, string splitting, path normalization,
filesystem semantics
Real-world Use Case: Normalizing file paths in shell utilities, web servers, and file managers.
Input Description: Function accepts an absolute Unix-style file path string.
Output Description: Returns the simplified canonical path.
Example Inputs and Outputs:
    path = "/a/./b/../../c/" -> "/c"
Constraints: Remove '.' segments, process '..' segments, and collapse redundant slashes.
Brute Force Approach: Parse characters manually with state.
Optimized Approach: Split by slash and process components with a stack.
Time Complexity: O(n)
Space Complexity: O(n)
Step-by-step Dry Run:
    split path, skip empty and '.', pop stack for '..', push normal segments.
Edge Cases: root-only path and trailing slashes.
Common Mistakes: leaving extra slashes or not handling too many '..'.
Follow-up Interview Questions:
    1. How would this work for relative paths?
    2. What if symbolic links should be resolved?
    3. Can you do this in place on a list of components?
Alternative Approaches: Use deque for segment processing.
Expected Output: The script prints simplified canonical paths for sample inputs.
Key Takeaways: Path normalization is a classic stack-based string problem.
"""

from __future__ import annotations

from typing import List


def simplify_path(path: str) -> str:
    parts = path.split('/')
    stack: List[str] = []
    for part in parts:
        if part == '' or part == '.':
            continue
        if part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)


def main() -> None:
    print('Simplified:', simplify_path('/a/./b/../../c/'))
    print('Simplified:', simplify_path('/home//foo/'))


if __name__ == '__main__':
    main()
