import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors)")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player} and the computer chose {computer}")
    if player == computer:
        return "it's a tie!"
    elif player == "rock" and computer == "scissors":
        return "rock smashes scissors! you win"
    elif player == "rock" and computer == "paper":
        return "paper covers rock! computer win"

check_win('rock','paper')