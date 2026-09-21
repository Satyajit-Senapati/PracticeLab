"""course_schedule.py

Problem Statement:
Implement a Python module that checks whether all courses can be finished
given prerequisite pairs.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: graph algorithms, cycle detection, topological sorting,
dependency resolution
Real-world Use Case: Task scheduling, build system dependency resolution,
course planning, and job orchestration.
Input Description: Functions accept the number of courses and prerequisite
pairs [course, prerequisite].
Output Description: Functions return True if all courses can be completed,
otherwise False.
Example Inputs and Outputs:
    can_finish(2, [[1,0]]) -> True
    can_finish(2, [[1,0],[0,1]]) -> False
Constraints: Use O(V + E) time and space. Detect cycles in directed graphs.
Brute Force Approach: Try all course orderings.
Optimized Approach: Use DFS with recursion stack or Kahn's algorithm.
Time Complexity: O(V + E)
Space Complexity: O(V + E)
Step-by-step Dry Run:
    num_courses = 2, prerequisites = [[1,0]]
    return True
Edge Cases: disconnected graphs, no prerequisites, and self-dependent
prerequisites.
Common Mistakes: missing cycle detection, using directed edges incorrectly,
and forgetting to handle isolated nodes.
Follow-up Interview Questions:
    1. How would you return a valid course ordering?
    2. Can you detect a cycle using DFS and color marking?
    3. What is the difference between Kahn's algorithm and DFS topo sort?
Alternative Approaches: Use Kahn's BFS-based topo sort or DFS recursion
stack marking.
Expected Output: The script prints feasibility for sample course schedules.
Key Takeaways: Cycle detection in directed graphs determines schedule
feasibility.
"""

from __future__ import annotations

from collections import defaultdict, deque
from typing import Dict, List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Return True if all courses can be completed given prerequisites."""
    graph: Dict[int, List[int]] = defaultdict(list)
    indegree: Dict[int, int] = {course: 0 for course in range(num_courses)}

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque([course for course, degree in indegree.items() if degree == 0])
    visited = 0

    while queue:
        node = queue.popleft()
        visited += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return visited == num_courses


def main() -> None:
    """Main function demonstrating course scheduling check."""
    examples = [
        (2, [[1, 0]]),
        (2, [[1, 0], [0, 1]]),
        (4, [[1, 0], [2, 1], [3, 2]]),
    ]
    for num_courses, prereqs in examples:
        print(f"num_courses={num_courses}, prereqs={prereqs} -> {can_finish(num_courses, prereqs)}")


if __name__ == "__main__":
    main()
