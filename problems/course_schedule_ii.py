"""course_schedule_ii.py

Problem Statement:
Implement a Python module that returns a valid order in which to take courses
given prerequisites.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: topological sorting, graph traversal, cycle detection,
dependency resolution
Real-world Use Case: Course planning, build systems, package dependency
management, and task orchestration.
Input Description: Functions accept the number of courses and prerequisite
pairs [course, prerequisite].
Output Description: Functions return a valid course order or an empty list if
no order exists.
Example Inputs and Outputs:
    find_order(2, [[1,0]]) -> [0, 1]
    find_order(2, [[1,0],[0,1]]) -> []
Constraints: Use O(V + E) time and space. Detect cycles and return a sequence
for all courses.
Brute Force Approach: Try every permutation of courses.
Optimized Approach: Use Kahn's algorithm for topological sort.
Time Complexity: O(V + E)
Space Complexity: O(V + E)
Step-by-step Dry Run:
    num_courses = 2, prerequisites = [[1,0]]
    order = [0, 1]
    return [0, 1]
Edge Cases: no prerequisites, impossible schedules, and disconnected
course graphs.
Common Mistakes: not handling isolated courses, returning partial order,
and missing cycle detection.
Follow-up Interview Questions:
    1. How would you return all valid course orders?
    2. What is the difference between Kahn's algorithm and DFS topo sort?
    3. How can this be adapted to build system dependency ordering?
Alternative Approaches: Use DFS with recursion stack while collecting a reverse
postorder.
Expected Output: The script prints valid course orders for sample inputs.
Key Takeaways: Topological sorting provides a valid sequence when dependencies
form a directed acyclic graph.
"""

from __future__ import annotations

from collections import defaultdict, deque
from typing import Dict, List


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """Return a valid course order or an empty list if no order exists."""
    graph: Dict[int, List[int]] = defaultdict(list)
    indegree: Dict[int, int] = {course: 0 for course in range(num_courses)}

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque([course for course, degree in indegree.items() if degree == 0])
    order: List[int] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_courses else []


def main() -> None:
    """Main function demonstrating valid course ordering."""
    examples = [
        (2, [[1, 0]]),
        (2, [[1, 0], [0, 1]]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
    ]
    for num_courses, prereqs in examples:
        print(f"num_courses={num_courses}, prereqs={prereqs} -> {find_order(num_courses, prereqs)}")


if __name__ == "__main__":
    main()
