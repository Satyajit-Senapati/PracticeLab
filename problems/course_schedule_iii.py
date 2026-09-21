"""course_schedule_iii.py

Problem Statement:
Implement a Python module that determines whether the course prerequisites
form a valid directed acyclic graph (DAG) and returns a valid course order if possible.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: graph traversal, topological sorting, cycle detection,
DFS recursion stack, dependency resolution
Real-world Use Case: Build system dependency ordering, course planning,
package install ordering, and task scheduling.
Input Description: Functions accept the number of courses and prerequisite
pairs [course, prerequisite].
Output Description: Functions return a valid ordering of courses or an empty
list if no valid ordering exists.
Example Inputs and Outputs:
    find_order(2, [[1,0]]) -> [0, 1]
    find_order(2, [[1,0],[0,1]]) -> []
Constraints: Use O(V + E) time and O(V + E) space. Detect directed cycles.
Brute Force Approach: Try all permutations and verify prerequisite satisfaction.
Optimized Approach: Use DFS with recursion stack or Kahn's algorithm.
Time Complexity: O(V + E)
Space Complexity: O(V + E)
Step-by-step Dry Run:
    graph edges: 0 -> 1
    order = [0, 1]
    return [0, 1]
Edge Cases: empty prerequisites, disconnected graphs, self-dependencies,
and graphs with cycles.
Common Mistakes: not checking recursion stack, using wrong edge direction,
and failing to include isolated courses in the result.
Follow-up Interview Questions:
    1. How can you detect a cycle while performing topological sort?
    2. What changes if there are multiple valid topological orders?
    3. How would you return a course order using DFS instead of BFS?
Alternative Approaches: Use DFS post-order traversal to build a reverse topological order.
Expected Output: The script prints course order results for sample inputs.
Key Takeaways: Topological sort solves dependency ordering when the graph is acyclic.
"""

from __future__ import annotations

from collections import defaultdict, deque
from typing import Dict, List


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """Return a valid course completion order or an empty list if impossible."""
    graph: Dict[int, List[int]] = defaultdict(list)
    indegree: Dict[int, int] = {course: 0 for course in range(num_courses)}

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque([course for course, degree in indegree.items() if degree == 0])
    order: List[int] = []

    while queue:
        current = queue.popleft()
        order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_courses else []


def main() -> None:
    """Main function demonstrating course ordering."""
    examples = [
        (2, [[1, 0]]),
        (2, [[1, 0], [0, 1]]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
    ]
    for num_courses, prerequisites in examples:
        print(
            f"num_courses={num_courses}, prerequisites={prerequisites} -> {find_order(num_courses, prerequisites)}"
        )


if __name__ == "__main__":
    main()
