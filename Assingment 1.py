"""
Author : Ali Ali
Student Number: 1005772
Due date : 28 February 2025
"""

"""
Part 1
Program : Even or Odd Predictor
Description : This program determines whether the product of two positive integers will be even or odd.

VARIABLE DICTIONARY :
num1 (int) = Stores the first user-input positive integer.
num2 (int) = Stores the second user-input positive integer.
"""

print("Even or Odd Product Predictor")
print("This program checks whether multiplying two positive whole numbers results in an even or odd product.")

# Get input from the user
num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))

# Check for even or odd product
if num1 % 2 == 0 or num2 % 2 == 0:
    print("Multiplying", num1, "by", num2, "results in an even product.")
else:
    print("Multiplying", num1, "by", num2, "results in an odd product.")
"""
Part 2
Program : Cube Diagonal Calculator
Description : This program calculates the inner diagonal of a cube using the provided edge length.

VARIABLE DICTIONARY :
edge_length (float) = The length of the cube’s edge provided by the user.
diagonal (float) = The calculated inner diagonal of the cube, rounded to two decimal places.
"""

import math

print("Cube Inner Diagonal Calculator")
print("This program calculates the inner diagonal (body diagonal) of a cube based on its edge length.")

# Get edge length from user
try:
    edge_length = float(input("Enter the edge length of the cube: "))
    # Calculate the diagonal
    diagonal = round(edge_length * math.sqrt(3), 2)
    print("A cube with an edge length of", edge_length, "has an inner diagonal of", diagonal)
except ValueError:
    print("Invalid input! Please enter a numerical value.")

"""
Part 3
Program : Coin Change Calculator
Description : This program determines the minimum number of coins needed to make change for an amount less than $1.00.

VARIABLE DICTIONARY :
change (int) = The amount of cents the user enters (converted to a value below 100 if necessary).
quarters (int) = The number of quarters needed.
dimes (int) = The number of dimes needed.
nickels (int) = The number of nickels needed.
pennies (int) = The number of pennies needed.
"""

print("Coin Change Calculator")
print("Enter an amount in cents (less than $1.00), and I will determine the minimum number of coins needed.")

# Get input from user and ensure it's within the valid range
change = int(input("Please enter the amount of change in cents: "))
change = change % 100  # Ensure it's below 100 cents

# Calculate the number of coins needed
quarters = change // 25
change %= 25
dimes = change // 10
change %= 10
nickels = change // 5
change %= 5
pennies = change

# Print the results
print("The minimum number of coins needed:", end=" ")
if quarters > 0:
    print(quarters, "quarter", end=" ")
if dimes > 0:
    print(dimes, "dime", end=" ")
if nickels > 0:
    print(nickels, "nickel", end=" ")
if pennies > 0:
    print(pennies, "penny", end=" ")
print()
