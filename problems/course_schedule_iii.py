"""course_schedule_iii.py

Problem Statement:
Choose the maximum number of courses that can be completed by their deadlines.
Each course is [duration, deadline]; take one course at a time starting on day
zero. Courses do not have prerequisites.
Interview Difficulty: Hard
Concepts Tested: greedy scheduling, max heap, deadline ordering
Input Description: A list of positive [duration, deadline] pairs.
Output Description: The maximum number of courses that can be completed.
Example Inputs and Outputs:
    schedule_course([[100,200],[200,1300],[1000,1250],[2000,3200]]) -> 3
Constraints: Course durations and deadlines are positive integers.
Time Complexity: O(n log n)
Space Complexity: O(n)
Edge Cases: no courses, impossible deadlines, replacing a long course.
"""

import heapq

def schedule_course(courses: list[list[int]]) -> int:
    """Keep the shortest feasible set for each deadline without mutating input."""
    durations = []
    elapsed = 0
    for duration, deadline in sorted(courses, key=lambda course: course[1]):
        if duration <= 0 or deadline <= 0:
            raise ValueError("Durations and deadlines must be positive.")
        elapsed += duration
        heapq.heappush(durations, -duration)
        if elapsed > deadline:
            elapsed += heapq.heappop(durations)
    return len(durations)


# Preserve the earlier prerequisite-ordering API for users of this source module.
def find_order(num_courses, prerequisites):
    from problems.course_schedule_ii import find_order as order_courses
    return order_courses(num_courses, prerequisites)


if __name__ == "__main__":
    print(schedule_course([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
