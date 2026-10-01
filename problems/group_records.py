"""group_records.py

Problem Statement:
Group mapping records by the value of a required field, preserving input order within each group. Raise KeyError when a record lacks the field. Leave input records unchanged.
Interview Difficulty: Easy
Concepts Tested: dictionaries, data grouping, records
Input Description: An iterable of dictionaries and a required field name; field values must be hashable.
Output Description: A dictionary mapping field values to lists of records.
Example Inputs and Outputs:
    group_records([{"team":"A","id":1},{"team":"B","id":2}], "team") -> {"A":[{"team":"A","id":1}],"B":[{"team":"B","id":2}]}
Constraints: An iterable of dictionaries and a required field name; field values must be hashable.
Time Complexity: O(n)
Space Complexity: O(n)
"""


def group_records(records, field: str) -> dict:
    result = {}
    for record in records:
        result.setdefault(record[field], []).append(record)
    return result
