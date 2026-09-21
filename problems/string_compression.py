"""string_compression.py

Problem Statement:
Implement a Python module that performs basic string compression using run
length encoding, demonstrating compression and decompression.

Interview Difficulty: Medium
Commonly Asked By: Amazon, Microsoft, Google, Adobe, Uber
Concepts Tested: string traversal, run-length encoding, edge-case handling,
round-trip correctness, simple compression algorithms
Real-world Use Case: Compacting repeated text, preprocessing log data,
compressing seasonal or repeated metadata fields, and encoding streaming
records.
Input Description: Functions accept a string to compress or decompress.
Output Description: Functions return compressed strings or decompressed outputs.
Example Inputs and Outputs:
    compress("aaabb") -> "a3b2"
    decompress("a3b2") -> "aaabb"
Constraints: Handle empty strings, single-character runs, and numeric counts.
Brute Force Approach: Build compressed output with repeated string multiplication.
Optimized Approach: Use sequential traversal with run-length encoding.
Time Complexity: O(n) for compression and decompression.
Space Complexity: O(n) for output strings.
Step-by-step Dry Run:
    input_text = "aabcc"
    compressed = "a2b1c2"
    return "a2b1c2"
Edge Cases: empty string, single-character string, large repeat counts, and
invalid compressed formats.
Common Mistakes: forgetting to flush the last run, assuming digits always
represent counts, and not validating decompressed input.
Follow-up Interview Questions:
    1. How would you modify this for case-sensitive text?
    2. Can you extend this to compress arbitrary binary data?
    3. What are the tradeoffs of run-length encoding?
Alternative Approaches: Use actual compression libraries like zlib for
production, or more advanced algorithms like Huffman coding.
Expected Output: The script prints compression and decompression results for
sample inputs.
Key Takeaways: Run-length encoding is a simple, easy-to-implement compression
strategy for repeated characters.
"""

from __future__ import annotations

from typing import List


def compress(text: str) -> str:
    """Compress a string using run-length encoding."""
    if not text:
        return ""

    compressed_parts: List[str] = []
    current_char = text[0]
    count = 1

    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            compressed_parts.append(f"{current_char}{count}")
            current_char = char
            count = 1
    compressed_parts.append(f"{current_char}{count}")

    compressed_text = "".join(compressed_parts)
    return compressed_text


def decompress(compressed_text: str) -> str:
    """Decompress a run-length encoded string."""
    if not compressed_text:
        return ""

    decompressed_parts: List[str] = []
    current_char: str = ""
    count_str: str = ""

    for char in compressed_text:
        if char.isalpha():
            if current_char and count_str:
                decompressed_parts.append(current_char * int(count_str))
            current_char = char
            count_str = ""
        elif char.isdigit():
            count_str += char
        else:
            raise ValueError("Invalid compressed format")

    if current_char and count_str:
        decompressed_parts.append(current_char * int(count_str))

    return "".join(decompressed_parts)


def main() -> None:
    """Main function demonstrating string compression."""
    examples = ["aaabb", "a", "abccc", ""]
    for example in examples:
        compressed_text = compress(example)
        decompressed_text = decompress(compressed_text)
        print(example, "->", compressed_text, "->", decompressed_text)


if __name__ == "__main__":
    main()
