"""EX05 - Dictionary Utility Functions."""

__author__ = "730462735"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    inverted: dict[str, str] = {}
    for key, value in d.items():
        if value in inverted:
            raise KeyError("You made a key mistake!")
        inverted[value] = key
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the most frequently occuring color from a dictionary."""
    color_count: dict[str, int] = {}
    max_count = 0
    max_color = ''
    for color in colors.values():
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1
        if color_count[color] > max_count or (color_count[color] == max_count and color < max_color):
            max_count = color_count[color]
            max_color = color
    return max_color


def count(values: list[str]) -> dict[str, int]:
    """Counts the frequencies of items in a list."""
    counts: dict[str, int] = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Categorizes words into lists based on their initial letter."""
    alphabetized: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in alphabetized:
            alphabetized[first_letter] = []
        alphabetized[first_letter].append(word)
    return alphabetized


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the attendance log with new attendance information."""
    if day in attendance_log:
        if student not in attendance_log[day]:  # Check if the student is already in the list
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]