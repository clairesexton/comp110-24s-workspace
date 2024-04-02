"""Splitting a dictionary into two lists!"""

__author__ = "730462735"


def get_keys(key_dict: dict[str, int]) -> list[str]:
    """Creating a list of existing dictionary keys."""
    return list(key_dict.keys())


def get_values(value_dict: dict[str, int]) -> list[int]:
    """Creating a list of existing dictionary values."""
    return list(value_dict.values())
