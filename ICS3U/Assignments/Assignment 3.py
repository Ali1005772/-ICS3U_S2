"""
Author         : Ali Ali
Student Number : 1005772

Revision Date  : 23 April 2025
Course Code    : ICS3U
Program        : Palindrome Checker
Description    : This program checks a list of words and determines which are palindromes.

VARIABLE DICTIONARY:
  words (list)         = Contains words to be evaluated for palindromicity
  word (string)        = The word currently being processed
  half (int)           = Half the length of the current word (for comparison)
  i (int)              = Loop index used to compare opposing characters
  left (char)          = Character from the beginning of the word
  right (char)         = Character from the end of the word
  is_palindrome (bool) = Flag to track if the word is a palindrome
"""

# Display a title for the user
print("=== Palindrome Checker ===")

# List of words to test
words = ["rotor", "banana", "refer", "robot", "racecar", "desk", "madam", "pilot", "noon", "stats"]

# Check each word in the list
for word in words:

    # Assume the word is a palindrome unless proven otherwise
    is_palindrome = True

    # Determine the midpoint of the word
    half = len(word) // 2

    # Check characters from both ends moving toward the center
    for i in range(half):
        left = word[i]
        right = word[-(i + 1)]

        # If characters don't match, it's not a palindrome
        if left != right:
            is_palindrome = False
            print(word, "is not a palindrome")
            break

    # If it passed all checks
    if is_palindrome:
        print(word, "is a palindrome")

# Closing message
print("=== End of check ===")
