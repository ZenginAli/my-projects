# Project 1.2 (Advanced Version)
# Rock Paper Scissors Game
# Date: 32.12.2025

# New Features:
# - Player name input
# - Free Mode / Fixed Rounds Mode
# - Statistics tracking
# - Final results screen


import random
import os
import time


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def map_choice(choice_number):
    return {0: "rock", 1: "paper", 2: "scissors"}[choice_number]


def get_player_choice():
    while True:
        choice = input("Choices: (R)ock, (P)aper, (S)cissors\nPick: ").lower()
        if choice in ["r", "p", "s"]:
            return map_choice({"r": 0, "p": 1, "s": 2}[choice])
        print("Invalid input. Please try again.")


def get_computer_choice():
    return map_choice(random.randint(0, 2))


def game_rules(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")
    ):
        return "player"
    else:
        return "computer"


# Get player name
def get_player_name():
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")


# Choose game mode
def choose_game_mode():
    while True:
        print("\nChoose game mode:")
        print("1 - Free Mode (play until you stop)")
        print("2 - Fixed Rounds Mode (set number of rounds)")
        choice = input("Select mode (1/2): ")

        if choice in ["1", "2"]:
            return choice
        print("Invalid selection. Try again.")


# Initialize statistics
def initialize_stats():
    return {
        "played": 0,
        "wins": 0,
        "losses": 0,
        "ties": 0,
        "points": 0
    }


# Update statistics
def update_stats(stats, result):
    stats["played"] += 1
    if result == "player":
        stats["wins"] += 1
        stats["points"] += 1
    elif result == "computer":
        stats["losses"] += 1
        stats["points"] -= 1
    else:
        stats["ties"] += 1


# Show final statistics
def show_final_results(player_name, stats):
    clear()
    win_rate = (stats["wins"] / stats["played"]) * 100 if stats["played"] > 0 else 0

    print("===== FINAL RESULTS =====\n")
    print(f"Player: {player_name}")
    print(f"Games Played : {stats['played']}")
    print(f"Wins         : {stats['wins']}")
    print(f"Losses       : {stats['losses']}")
    print(f"Ties         : {stats['ties']}")
    print(f"Win Rate     : {win_rate:.2f}%")
    print(f"Points       : {stats['points']}\n")

    if stats["points"] > 0:
        print(f"Winner: {player_name}")
    elif stats["points"] < 0:
        print("Winner: Computer")
    else:
        print("Result: Draw")


def play_game():
    clear()
    player_name = get_player_name()
    stats = initialize_stats()

    clear()
    mode = choose_game_mode()
    clear()

    # FREE MODE
    if mode == "1":
        while True:
            player_choice = get_player_choice()
            computer_choice = get_computer_choice()

            print(f"\nComputer chose: {computer_choice}")
            print(f"{player_name} chose: {player_choice}")

            result = game_rules(player_choice, computer_choice)
            update_stats(stats, result)

            if result == "player":
                print(f"\nResult: {player_name} wins!")
            elif result == "computer":
                print("\nResult: Computer wins!")
            else:
                print("\nResult: It's a tie!")

            time.sleep(1.5)

            while True:
                again = input("\nPlay another round? (y/n): ").lower()
                if again == "y":
                    clear()
                    break
                elif again == "n":
                    return show_final_results(player_name, stats)
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

    # FIXED ROUNDS MODE
    else:
        while True:
            try:
                rounds = int(input("How many rounds do you want to play? "))
                if rounds > 0:
                    break
                print("Number must be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")

        for round_number in range(1, rounds + 1):
            clear()
            print(f"Round {round_number} / {rounds}\n")

            player_choice = get_player_choice()
            computer_choice = get_computer_choice()

            print(f"\nComputer chose: {computer_choice}")
            print(f"{player_name} chose: {player_choice}")

            result = game_rules(player_choice, computer_choice)
            update_stats(stats, result)

            if result == "player":
                print(f"\nResult: {player_name} wins!")
            elif result == "computer":
                print("\nResult: Computer wins!")
            else:
                print("\nResult: It's a tie!")

            input("\nPress Enter to continue...")

        show_final_results(player_name, stats)


# Start the game
play_game()
