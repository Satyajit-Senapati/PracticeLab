"""generators.py

Problem Statement:
Implement a Python module that demonstrates generator functions and generator
expressions for memory-efficient iteration, lazy evaluation, and streaming data
processing.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: generators, yield, generator expressions, lazy evaluation,
iterator protocol, memory efficiency, stream processing
Real-world Use Case: Processing large datasets, streaming log files,
transforming ETL records on the fly, generating infinite sequences, and
building pipelines for data ingestion.
Input Description: Functions accept iterables, numeric values, and optional
transformation functions to generate streamed output lazily.
Output Description: The functions return generator objects or iterated
results that can be consumed without loading all elements into memory.
Example Inputs and Outputs:
    even_numbers_generator(5) -> 0, 2, 4
    range_squared_generator(3) -> 0, 1, 4
    stream_transform([1, 2, 3], lambda x: x * 2) -> 2, 4, 6
Constraints: Use generators for lazy iteration, avoid materializing large
collections when possible, and keep generator logic simple and composable.
Brute Force Approach: Build intermediate lists and iterate over them.
Optimized Approach: Yield values directly from generators and compose
transformations using generator expressions.
Time Complexity: O(n) to iterate through n items.
Space Complexity: O(1) additional space for generator state, O(n) only when
results are explicitly materialized.
Step-by-step Dry Run:
    sequence = range_squared_generator(3)
    yield 0
    yield 1
    yield 4
    return generator
Edge Cases: empty iterables, infinite generators, consumer not exhausting
generator, and generator state after partial consumption.
Common Mistakes: using list comprehensions instead of generator expressions,
returning a list from a generator function, and reusing exhausted generators.
Follow-up Interview Questions:
    1. How do generators differ from iterators?
    2. When should you use a generator expression versus a list comprehension?
    3. How can generators improve memory usage in data pipelines?
Alternative Approaches: Use explicit iterator classes, async generators for
asynchronous streams, or batch processing when processing by chunks.
Expected Output: The script prints sample values produced by generators and
shows how lazy evaluation works through streaming transformations.
Key Takeaways: Generators provide memory-efficient iteration and are ideal
for building composable, lazy data processing pipelines.
"""

from __future__ import annotations

from typing import Callable, Generator, Iterable, Iterator, Sequence


def even_numbers_generator(limit: int) -> Generator[int, None, None]:
    """Yield even numbers from 0 up to the specified limit (exclusive)."""
    number = 0
    while number < limit:
        yield number
        number += 2


def range_squared_generator(limit: int) -> Generator[int, None, None]:
    """Yield squared values for integers from 0 to limit - 1."""
    for value in range(limit):
        yield value * value


def stream_transform(
    values: Iterable[int],
    transform: Callable[[int], int],
) -> Generator[int, None, None]:
    """Lazily transform values from an iterable using the provided function."""
    for value in values:
        yield transform(value)


def filter_positive_generator(values: Iterable[int]) -> Generator[int, None, None]:
    """Yield only positive values from the input iterable."""
    for value in values:
        if value > 0:
            yield value


def chunked_generator(values: Sequence[int], chunk_size: int) -> Generator[Sequence[int], None, None]:
    """Yield chunks of the input sequence with a fixed size."""
    for start in range(0, len(values), chunk_size):
        yield values[start : start + chunk_size]


def generator_expression_example(values: Iterable[int]) -> Generator[int, None, None]:
    """Return a generator expression that yields doubled values."""
    return (value * 2 for value in values)


def consume_generator(generator: Iterator[int], max_items: int) -> list[int]:
    """Consume up to max_items from a generator and return a list."""
    results: list[int] = []
    for index, value in enumerate(generator):
        if index >= max_items:
            break
        results.append(value)
    return results


def main() -> None:
    """Main function demonstrating generator usage."""
    evens = list(even_numbers_generator(10))
    squares = list(range_squared_generator(5))
    transformed = list(stream_transform([1, 2, 3], lambda value: value * 2))
    positives = list(filter_positive_generator([-2, -1, 0, 1, 2, 3]))
    chunks = list(chunked_generator([1, 2, 3, 4, 5, 6], 2))
    doubled = list(generator_expression_example([1, 2, 3]))
    partial_consume = consume_generator(range_squared_generator(10), 3)

    print("Even numbers:", evens)
    print("Squared values:", squares)
    print("Transformed values:", transformed)
    print("Positive values:", positives)
    print("Chunked values:", chunks)
    print("Doubled values from generator expression:", doubled)
    print("Partial generator consumption:", partial_consume)


if __name__ == "__main__":
    main()
