import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ")
    user_choice = user_choice.lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ")
        user_choice = user_choice.lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        return "Congratulations! You win!"
    else:
        return "Sorry, you lose!"

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()
