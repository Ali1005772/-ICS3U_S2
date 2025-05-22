# Define the add function that returns the sum of two inputs
def add(a, b):
    sum = a + b
    return sum

# Step 1: Test add with integers
result = add(7, 2)
print(result)  # Expected output: 9
print(type(result))  # Expected type: <class 'int'>

# Step 2: Test add with floats
result = add(7.0, 2.0)
print(result)  # Expected output: 9.0
print(type(result))  # Expected type: <class 'float'>

# Step 3: Test add with strings
result = add("7", "2")
print(result)  # Expected output: "72" (string concatenation)
print(type(result))  # Expected type: <class 'str'>

result = add("book", "keeper")
print(result)  # Expected output: "bookkeeper"
print(type(result))  # Expected type: <class 'str'>

# Step 4: Define a function to get absolute value (int or float)
def myAbs(n):
    if n < 0:
        return -n
    else:
        return n

# Test the myAbs function
b = -12
a = myAbs(b)
print("The absolute value of %d is %d" % (b, a))  # Output: The absolute value of -12 is 12

b = 5.2
a = myAbs(b)
print("The absolute value of %.1f is %.1f" % (b, a))  # Output: The absolute value of 5.2 is 5.2

b = -5.2
a = myAbs(b)
print("The absolute value of %.1f is %.1f" % (b, a))  # Output: The absolute value of -5.2 is 5.2
