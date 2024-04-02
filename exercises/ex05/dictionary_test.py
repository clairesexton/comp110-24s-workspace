"""Testing the dictionary created in EX05."""

__author__ = "730462735"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
 
import pytest


# Testing invert function
def test_invert_expected_use_case() -> None:
    """Test invert function with expected use case."""
    my_dictionary = {'A': '1', 'B': '2', 'C': '3'}
    inverted_dict = invert(my_dictionary)
    assert inverted_dict == {'1': 'A', '2': 'B', '3': 'C'}


def test_invert_empty_dict() -> None:
    """Test invert function with an empty dictionary."""
    my_dictionary = {}
    inverted_dict = invert(my_dictionary)
    assert inverted_dict == {}


def test_invert_duplicate_values() -> None:
    """Test invert function with duplicate values."""
    with pytest.raises(KeyError):
        my_dictionary = {'A': '1', 'B': '1'}
        invert(my_dictionary)


# Testing favorite_color function
def test_favorite_color_expected_use_case() -> None:
    """Test favorite_color function with expected use case."""
    my_dictionary = {'Alice': 'Blue', 'Bob': 'Green', 'Charlie': 'Red'}
    assert favorite_color(my_dictionary) == 'Blue'


def test_favorite_color_empty_dict() -> None:
    """Test favorite_color function with an empty dictionary."""
    my_dictionary = {}
    assert favorite_color(my_dictionary) == ''


def test_favorite_color_multiple_max() -> None:
    """Test favorite_color function with multiple colors having the maximum frequency."""
    my_dictionary = {'Alice': 'Blue', 'Bob': 'Green', 'Charlie': 'Red', 'David': 'Blue'}
    assert favorite_color(my_dictionary) == 'Blue'


# Testing count function
def test_count_expected_use_case() -> None:
    """Test count function with expected use case."""
    my_list = ['apple', 'banana', 'apple', 'orange', 'apple']
    assert count(my_list) == {'apple': 3, 'banana': 1, 'orange': 1}


def test_count_empty_list() -> None:
    """Test count function with an empty list."""
    my_list = []
    assert count(my_list) == {}


def test_count_duplicate_items() -> None:
    """Test count function with duplicate items."""
    my_list = ['apple', 'banana', 'apple', 'banana', 'apple']
    assert count(my_list) == {'apple': 3, 'banana': 2}


# Testing alphabetizer function
def test_alphabetizer_expected_use_case() -> None:
    """Test alphabetizer function with expected use case."""
    my_list = ['apple', 'banana', 'cherry', 'apricot', 'blueberry']
    assert alphabetizer(my_list) == {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}


def test_alphabetizer_empty_list() -> None:
    """Test alphabetizer function with an empty list."""
    my_list = []
    assert alphabetizer(my_list) == {}


def test_alphabetizer_mixed_case() -> None:
    """Test alphabetizer function with mixed-case words."""
    my_list = ['Apple', 'banana', 'Cherry', 'apricot', 'blueberry']
    assert alphabetizer(my_list) == {'a': ['Apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['Cherry']}


# Testing update_attendance function
def test_update_attendance_expected_use_case() -> None:
    """Test update_attendance function with expected use case."""
    attendance = {'Monday': ['Anna'], 'Tuesday': ['Anna']}
    update_attendance(attendance, 'Monday', 'Eve')
    assert attendance == {'Monday': ['Anna', 'Eve'], 'Tuesday': ['Anna']}


def test_update_attendance_new_day() -> None:
    """Test update_attendance function with a new day."""
    attendance = {'Monday': ['Anna'], 'Tuesday': ['Anna']}
    update_attendance(attendance, 'Wednesday', 'Eve')
    assert attendance == {'Monday': ['Anna'], 'Tuesday': ['Anna'], 'Wednesday': ['Eve']}


def test_update_attendance_multiple_students() -> None:
    """Test update_attendance function with multiple students."""
    attendance = {'Monday': ['Anna'], 'Tuesday': ['Anna']}
    update_attendance(attendance, 'Monday', 'Eve')
    update_attendance(attendance, 'Tuesday', 'Bob')
    assert attendance == {'Monday': ['Anna', 'Eve'], 'Tuesday': ['Anna', 'Bob']}


if __name__ == "__main__":
    pytest.main()