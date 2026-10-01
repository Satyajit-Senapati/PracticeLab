"""word_pattern_ii.py

Problem Statement:
Match each pattern character to a non-empty substring so concatenating the
mapped substrings reproduces text. Different characters must map to different
substrings. This problem does not split text into words.
Interview Difficulty: Hard
Concepts Tested: backtracking, bijective mapping, string partitioning
Input Description: A pattern and an unseparated text string.
Output Description: True when a bijective substring mapping exists.
Example Inputs and Outputs:
    word_pattern_match("abab", "redblueredblue") -> True
    word_pattern_match("ab", "aa") -> False
Constraints: Map every pattern character to a non-empty substring.
Time Complexity: Exponential in the text length.
Space Complexity: O(n + p) for text length n and pattern length p.
Edge Cases: empty strings, repeated characters, conflicting mappings.
"""

def word_pattern_match(pattern: str, text: str) -> bool:
    """Find a bijection from pattern characters to non-empty substrings."""
    mapping, used = {}, set()
    def search(pi, ti):
        if pi == len(pattern):
            return ti == len(text)
        if len(text) - ti < len(pattern) - pi:
            return False
        char = pattern[pi]
        if char in mapping:
            word = mapping[char]
            return text.startswith(word, ti) and search(pi + 1, ti + len(word))
        for end in range(ti + 1, len(text) + 1):
            word = text[ti:end]
            if word in used:
                continue
            mapping[char] = word
            used.add(word)
            if search(pi + 1, end):
                return True
            used.remove(word)
            del mapping[char]
        return False
    return search(0, 0)
