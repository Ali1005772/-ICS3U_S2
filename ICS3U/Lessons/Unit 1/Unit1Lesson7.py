# Palindrome input/output and conditionals lesson example
# Program to check if one number is a factor of another with full input validation

# Ask for the first number
x = input("Please input a whole number between 1 and 20: ")
x = int(x)

# Check if x is in the valid range
if x < 1 or x > 20:
    print(x, "is outside of range. Cannot continue.")
else:
    # Ask for the second number
    y = input("Please input another whole number between 1 and 20: ")
    y = int(y)

    # Check if y is in the valid range
    if y < 1 or y > 20:
        print(y, "is outside of range. Cannot continue.")
    else:
        print("Now deciding if", y, "is a factor of", x, "...")

        # Check for division by zero — although 0 is already excluded, we include this for completeness
        if y != 0:
            rem = x % y
            if rem == 0:
                print("Yes!", y, "is a factor of", x, "!")
            else:
                print(y, "is not a factor of", x, ".")
        else:
            # This case won't actually happen due to range validation, but is good practice
            print("Cannot divide by zero. A factor could not be determined.")
