import random

def guess():
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    target_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    while True:
        attempts += 1
        guess = int(input("Enter your guess: "))
        if guess == target_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < target_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

guess()
