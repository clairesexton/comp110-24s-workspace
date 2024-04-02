"""Mutating functions."""

__author__ = "730462735"


def manual_append(input: list(int), mod: int) -> None:
    """Appends mod to end."""
    input.append(mod)
    return


def double(input: list(int)) -> None:
    """Multiplies input by 2."""
    i: int = 0
    while i < len(input):
        input[i] = input[i] * 2
        i += 1
    return