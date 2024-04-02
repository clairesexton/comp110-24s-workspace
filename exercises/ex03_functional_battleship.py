"""EX03 - Functional Battleship - A two-player game!"""

__author__ = "730462735"

import random


def input_guess(grid_size: int, coordinate_type: str) -> int:
    """User must input guess"""
    assert coordinate_type == "row" or coordinate_type == "column", "Invalid coordinate type. Must be 'row' or 'column'."
    attempt = 0
    while True:
        if attempt == 0:
            guess = int(input(f"Guess a {coordinate_type}: "))
        else:
            guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        if 1 <= guess <= grid_size:
            return guess
        attempt += 1


def print_grid(grid_size: int, row_input: int, column_input: int, correct_guess: bool) -> None:
    """Printing the grid based on the parameters given."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    result: str = RED_BOX if correct_guess else WHITE_BOX
    row_count: int = 1
    while row_count <= grid_size:
        row_str: str = ""
        column_count: int = 1
        while column_count <= grid_size:
            row_str += result if column_input == column_count and row_input == row_count else BLUE_BOX
            column_count += 1
        print(row_str)
        row_count += 1


def correct_guess(secret_row: int, secret_column: int, row_input: int, column_input: int) -> bool:
    """Checking to see if the secret location matches the location guessed."""
    return secret_row == row_input and secret_column == column_input


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Time to run the main loop."""
    turn_count: int = 0
    turn_max: int = 5
    win: bool = False

    while turn_count < turn_max and not win:
        turn_count += 1
        print(f"=== Turn {turn_count}/{turn_max} ===")
        row_input = input_guess(grid_size, "row")
        column_input = input_guess(grid_size, "column")
        the_correct_guess = correct_guess(secret_row, secret_column, row_input, column_input)
        print_grid(grid_size, row_input, column_input, the_correct_guess)
        if the_correct_guess:
            print(f"Hit! You won in {turn_count}/{turn_max} turns!")
            win = True
        else:
            print("Miss!")
            
    if not win:
        print(f"X/{turn_max} - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))