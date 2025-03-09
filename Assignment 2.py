"""
Student Name: Ali Ali
Student Number: 1005772
Course Code: ICS3U

Program Description:
This is a number guessing game where the user tries to guess a randomly generated number 
within six attempts. After each incorrect guess, the program provides hints to help the user.

Variable Dictionary:
secret_number - The target number the user must guess (int)
attempts - Number of attempts made by the user (int)
max_attempts - The maximum number of attempts allowed (int)
guess - The user's guessed number (int)
is_correct - A flag to determine if the user guessed correctly (boolean)
"""
import random

# Game initialization
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 6
is_correct = False  # Track if the user has guessed correctly

# Display welcome message
print("=== Number Guessing Game ===")
print("Try to guess the number I have chosen between 1 and 100!")
print("You have", max_attempts, "attempts to find the correct number.")

# Game loop
while attempts < max_attempts and not is_correct:
    print("Attempt", attempts + 1, "of", max_attempts, ":")
    user_input = input()
    
    # Convert input directly without checking
    guess = int(user_input)
    attempts += 1

    if guess == secret_number:
        print("Awesome! You guessed the number correctly!")
        is_correct = True  # Set flag to True
    elif guess < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")

# If user fails to guess correctly within max attempts
if not is_correct:
    print("You've used all", max_attempts, "attempts! The correct number was", secret_number, ". Better luck next time!")
