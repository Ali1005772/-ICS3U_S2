# ----------- Menu Program Section -----------

# Display menu options for the user
print("Make a choice from the following menu:")
print("A: apples")
print("B: bananas")
print("C: cherries")

# Get user input for their choice
ch = input("Your choice: ")

# Use if-elif-else to handle valid and invalid choices
if ch == "A":
    print("I prefer apples")
elif ch == "B":
    print("I prefer bananas")
elif ch == "C":
    print("I prefer cherries")
else:
    print("Invalid choice. Please enter A, B, or C.")

# ----------- Compound Conditional Example -----------

# Set up values for testing compound conditionals
A = B = 10   # Assign 10 to both A and B
C = D = 50   # Assign 50 to both C and D

# Check if both conditions are true using and
if (A == B) and (C == D):
    print("Hooray!")
else:
    print("Boo!")

# ----------- Marking System Section -----------

# Ask for a mark input
mark_input = input("Enter a mark from 1 to 100: ")

# Convert the input string to an integer
mark = int(mark_input)

# Use compound conditionals to determine the letter grade
if (mark >= 80) and (mark <= 100):
    print("You got an A")
elif (mark >= 70) and (mark <= 79):
    print("You got a B")
elif (mark >= 60) and (mark <= 69):
    print("You got a C")
elif (mark >= 50) and (mark <= 59):
    print("You got a D")
elif (mark >= 0) and (mark < 50):
    print("You got an F")
else:
    print("That is not a valid mark.")
