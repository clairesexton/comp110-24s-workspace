"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730462735"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Convert input to an integer
player1_input = int(input("Pick a secret boat location between 1 and 4:"))

if player1_input < 1:
    print(f"Error! {player1_input} too low!")
    exit()
elif player1_input > 4:
    print(f"Error! {player1_input} too high!")
    exit()

player2_input = int(input("Guess a number between 1 and 4:"))

if player2_input < 1:
    print(f"Error! {player2_input} too low!")
    exit()
elif player2_input > 4:
    print(f"Error! {player2_input} too high!")
    exit()

if player1_input == player2_input:
    result = RED_BOX
    print("Correct! You hit the ship.")
else:
    result = WHITE_BOX
    print("Incorrect! You missed the ship.")

emoji_boxes = ""

if player2_input == 1:
    emoji_boxes += result  
else:
    emoji_boxes += BLUE_BOX 

if player2_input == 2:
    emoji_boxes += result  
else:
    emoji_boxes += BLUE_BOX  

if player2_input == 3:
    emoji_boxes += result  
else:
    emoji_boxes += BLUE_BOX  

if player2_input == 4:
    emoji_boxes += result  
else:
    emoji_boxes += BLUE_BOX  

print(emoji_boxes)