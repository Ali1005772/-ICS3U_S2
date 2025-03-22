"""
Student Name: Ali Ali
Student Number: 1005772
Course Code: ICS3U

Program Description:
This is a number guessing game where the user tries to guess a randomly generated number 
within six attempts. After each incorrect guess, the program provides hints to help the user.

Variable Dictionary:

secret_number – The target number randomly chosen between 1 and 100 that the user must guess (int)
max_attempts – The maximum number of guesses allowed for the user (int)
attempts – The number of guesses the user has made so far (int)
is_correct – A flag that becomes True when the user guesses the correct number (boolean)
current_attempt – The current attempt number used for display purposes (int)
user_input – The raw input entered by the user (str)
is_valid – Indicates whether the user's input is a valid positive whole number (boolean)
guess – The user’s input converted into an integer, used to compare against the secret number (int)

"""
# Import the random module to generate a random number
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the maximum number of allowed guesses
max_attempts = 6

# Initialize the attempt counter
attempts = 0

# Track whether the correct guess has been made
is_correct = False

# Show the game title
print("=== Number Guessing Game ===")

# Explain the goal
print("Try to guess the number I have chosen between 1 and 100!")

# Show allowed attempts
print("You have", max_attempts, "attempts to find the correct number.")

# Loop while attempts remain and number isn't guessed
while attempts < max_attempts and not is_correct:

    # Calculate the current attempt number (1-based)
    current_attempt = attempts + 1

    # Display attempt number
    print("Attempt", current_attempt, "of", max_attempts, ":")

    # Get input from the user
    user_input = input()

    # Check if input is a positive whole number
    is_valid = user_input.isdigit()

    # If input is valid
    if is_valid:

        # Convert the string input to an integer
        guess = int(user_input)

        # Increase the attempt counter
        attempts = attempts + 1

        # If the guess is correct
        if guess == secret_number:

            # Congratulate the user
            print("Awesome! You guessed the number correctly!")

            # Set flag to exit loop
            is_correct = True

        # If the guess is too low
        elif guess < secret_number:

            # Prompt user to go higher
            print("Try a higher number.")

        # If the guess is too high
        else:

            # Prompt user to go lower
            print("Try a lower number.")

    # If input is not valid
    else:

        # Inform the user about invalid input
        print("Invalid input. Please enter a whole number.")

# If the correct number wasn't guessed in time
if not is_correct:

    # Reveal the number and end the game
    print("You've used all", max_attempts, "attempts! The correct number was", secret_number, ". Better luck next time!")

