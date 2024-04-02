"""Test my garden functions."""

__author__ = "730462735"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date

def test_add_by_kind() -> None:
    """Testing the add_by_kind function with an edge case."""
    garden: dict[str, list[str]] = {"trees": ["oak", "maple"]}
    new_plant_kind1: str = "trees"
    new_plant: str = "willow"
    add_by_kind(garden, new_plant_kind1, new_plant)
    assert garden == {"trees": ["oak", "maple", "willow"]}


def test_add_by_kind() -> None:
    """Testing the add_by_kind function with a use case."""
    garden2: dict[str, list[str]] = {"fruit": ["apple", "orange"]}
    plant_kind: str = "herbs"
    new_plant_kind2: str = "thyme"
    add_by_kind(garden2, plant_kind, new_plant_kind2)
    assert garden2 == {"fruit": ["apple", "orange"], "herbs": ["thyme"]}


def test_add_by_date() -> None:
    """Tests add_by_date function with an edge case."""
    garden00: dict[str, list[str]] = {"June": ["cucumbers", "carrots"]}
    date_kind: str = "June"
    new_plant00: str = "squash"
    add_by_date(garden00, date_kind, new_plant00)
    assert garden00 == {"June": ["cucumbers", "carrots", "squash"]}


def test_add_by_date() -> None:
    """Tests add_by_date function with a use case."""
    garden01: dict[str, list[str]] = {"July": ["rosemary", "tomatoes"]}
    date_kind01: str = "August"
    new_plant01: str = "zucchini"
    add_by_date(garden01, date_kind01, new_plant01)
    assert garden01 == {"July": ["rosemary", "tomatoes"], "August": ["zucchini"]}


def test_lookup_by_kind_and_date() -> None:
    """Tests lookup_by_kind_and_date function with an edge case."""
    garden: dict[str, list[str]] = {"trees": ["oak", "hickory"], "flowers": ["rose"]}
    kind: str = "flowers"
    date: str = "March"
    assert lookup_by_kind_and_date(garden, kind, date) == []


def test_lookup_by_kind_and_date() -> None:
    """Tests lookup_by_kind_and_date function with a use case."""
    garden: dict[str, list[str]] = {"trees": ["oak", "maple"], "flowers": ["rose", "tulip"]}
    kind: str = "trees"
    date: str = "April"
    assert lookup_by_kind_and_date(garden, kind, date) == ["oak", "maple"]


if __name__ == "__main__":
    import lessons.garden.garden_helpers_test
