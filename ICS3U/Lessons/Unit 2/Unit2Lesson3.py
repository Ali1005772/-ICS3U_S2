# Unit 2 - Lesson 3: The Factorial

print("Factorial Calculator:")

# Get input from user for upper limit n
n = int(input("Enter a value for the upper limit, n: "))

# Part 1: Calculate and print factorial of just n
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("%d! = %d" % (n, factorial))

# Part 2: Calculate and print factorials from 0! up to n!
# By definition, 0! = 1
print("0! = 1")  # zero factorial
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print("%d! = %d" % (i, factorial))
