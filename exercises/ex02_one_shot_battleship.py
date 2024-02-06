"""EX02 - One Shot Battleship - A step closer to real battleship"""

__author__ = "730462735"

#Declaring the emoji variables
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

#Declaring the grid variables
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
row_counter: int = 1

#First ask user to guess row and column
player_input_row = int(input("Guess a row:"))
while player_input_row < 0 or player_input_row > grid_size:
    print(f"The grid is only {grid_size} by {grid_size}. Try again:")
    player_input_row = int(input())

player_input_col = int(input("Guess a column: "))
while player_input_col < 0 or player_input_col > grid_size:
    print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
    player_input_col = int(input())

#Then print grid based on user response  
result = ""
if player_input_row == secret_row and player_input_col == secret_column:
      result = RED_BOX
else:
      result = WHITE_BOX
    # Check if guess matches secret
while row_counter <= grid_size:
      emoji_row = ""
      column_counter = 1
      if row_counter == player_input_row:
        while column_counter <= grid_size:
                  if column_counter == player_input_col:
                        emoji_row += result
                  else: 
                        emoji_row += BLUE_BOX
                  column_counter += 1
      else:
        
            while column_counter <= grid_size:
                  emoji_row += BLUE_BOX
                  column_counter += 1
      print(emoji_row)
      row_counter += 1

#Add a comment under grid describing if user was accurate or not
if player_input_row == secret_row and player_input_col == secret_column:
        print("Hit!")
elif player_input_col == secret_column and player_input_row != secret_row:
      print("Close! Correct column, wrong row.")
elif player_input_col != secret_column and player_input_row==player_input_row:
      print("Close! Correct row, wrong column.")
else:
        print("Miss!")




                  




                