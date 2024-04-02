"""Summing the elements of a list using different loops"""

__author__ = "730462735"


def w_sum(vals: list[float]) -> float:
    """Calculate the sum of elements in vals using a while loop."""
    total = 0.0
    index = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Calculate the sum of elements in vals using a for-in loop."""
    total = 0.0
    for val in vals:
        total += val
    return total


def f_range_sum(vals: list[float]) -> float:
    """Calculate the sum of elements in vals using a for-in-range loop."""
    total = 0.0
    for i in range(len(vals)):
        total += vals[i]
    return total


# Test cases
print(w_sum([1.1, 0.9, 1.0]))  # Output should be 3.0
print(w_sum([]))  # Output should be 0.0
print(f_sum([1.1, 0.9, 1.0]))  # Output should be 3.0
print(f_sum([]))  # Output should be 0.0
print(f_range_sum([1.1, 0.9, 1.0]))  # Output should be 3.0
print(f_range_sum([]))  # Output should be 0.0
