"""merge_sorted_iterators.py

Problem Statement:
Merge any number of sorted iterables lazily. Yield ascending values, retaining duplicates, without materializing the input streams.
Interview Difficulty: Medium
Concepts Tested: generators, iterators, heap, lazy evaluation
Input Description: Any number of ascending iterables of comparable values.
Output Description: An iterator of ascending values.
Example Inputs and Outputs:
    list(merge_sorted_iterators([1,4], [2,3])) -> [1,2,3,4]
Constraints: Any number of ascending iterables of comparable values.
Time Complexity: O(n log k) for n items from k streams
Space Complexity: O(k)
"""

import heapq

def merge_sorted_iterators(*iterables):
    heap = []
    for index, iterable in enumerate(iterables):
        iterator = iter(iterable)
        try:
            heapq.heappush(heap, (next(iterator), index, iterator))
        except StopIteration:
            pass
    while heap:
        value, index, iterator = heapq.heappop(heap)
        yield value
        try:
            heapq.heappush(heap, (next(iterator), index, iterator))
        except StopIteration:
            pass
