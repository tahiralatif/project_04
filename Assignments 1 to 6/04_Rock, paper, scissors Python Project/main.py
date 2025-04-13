# rock, paper, scisssor

import random

def main():
    try:
        user_input = input("Enter your choice (rock, paper, scissors)").lower()
        choices = ["rock", "paper", "scissors"]
        computer_input = random.choice(choices)

        print(f"you chose {user_input} compuer choose {computer_input}" )

        if user_input == computer_input:
            print("It's a tie! as both selected {computer_input}")
        elif user_input == "rock":
            if computer_input == "scissors":
                print("You win! Rock crushes scissors.")
            else:
                print("You lose! Paper covers rock.")
        elif user_input == "paper":
            if computer_input == "rock":
                print("You win! Paper covers rock.") 
            else:
                print("You lose! Scissors cuts paper.")
        elif user_input == "scissors":
            if computer_input == "paper":
                print("You win! Scissors cuts paper.")
            else:
                print("You lose! Rock crushes scissors.") 
        else:
            print("Invalid input! Please enter rock, paper, or scissors.")
    except TypeError:
        print("Invalid input! Please enter rock, paper, or scissors.")                                    