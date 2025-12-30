# Projekt 1 
# Rock Paper Scissors Game
# 30.12.2025

import random
import os
import time

# Clear the terminal screen for better user experience
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Set of instructions for Rock-Paper-Scissors
def rps_instructions():
    """Print the instructions for Rock-Paper-Scissors."""
    print("Instructions for Rock-Paper-Scissors:")
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")

# Function to map choices to string (rock, paper, scissors)
def map_choice(choice_number):
    """Map number (0-2) to the corresponding game move."""
    game_map = {0: "rock", 1: "paper", 2: "scissors"}
    return game_map[choice_number]

# Check game rules and determine the result
def game_rules(player_choice, computer_choice):
    """Check who wins the game."""
    if player_choice == computer_choice:
        return "It's a tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "Player wins!"
    else:
        return "Computer wins!"

# Function to get player input and ensure it's valid
def get_player_choice():
    """Get player input and validate it."""
    while True:
        player_choice = input('Choices: (R)ock, (P)aper, (S)cissors\nPick: ').lower()
        if player_choice in ['r', 'p', 's']:
            return map_choice({'r': 0, 'p': 1, 's': 2}[player_choice])
        else:
            print("Invalid input! Please choose Rock, Paper, or Scissors.")

# Function to get computer's choice
def get_computer_choice():
    """Get computer's choice randomly."""
    return map_choice(random.randint(0, 2))

def play_game():
    """Run the game logic, display results."""
    clear()  # Clear the screen at the start of the game
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    
    # Result Page
    print(f"\nComputer chooses: {computer_choice.capitalize()}")
    print(f"Player chooses: {player_choice.capitalize()}")
    
    result = game_rules(player_choice, computer_choice)
    print(f"\nResult: {result}")
    
    time.sleep(9)

# Call play_game function to start the game
play_game()
   