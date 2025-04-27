
import random

# The computer selects a random number between 0 and 99
number_to_guess = random.randint(0, 99)

# Initialize the guess
guess = None

# Loop until the user guesses correctly
while guess != number_to_guess:
    # Prompt the user for a guess
    guess = int(input("Enter a guess: "))
    
    # Check if the guess is too high or too low
    if guess > number_to_guess:
        print("Your guess is too high")
    elif guess < number_to_guess:
        print("Your guess is too low")
    else:
        print(f"Congrats! The number was: {number_to_guess}")
