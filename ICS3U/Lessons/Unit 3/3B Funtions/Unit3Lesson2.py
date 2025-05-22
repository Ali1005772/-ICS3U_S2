import math

# Function to factorize N and return a list of proper factors (excluding N itself)
def factorize(N):
    factors = [1] if N > 1 else []  # 1 is a proper factor of any number > 1
    limit = int(math.sqrt(N))
    
    for i in range(2, limit + 1):
        if N % i == 0:
            factors.append(i)
            other_factor = N // i
            if other_factor != i and other_factor != N:
                factors.append(other_factor)
    return factors

# Function to sum the elements of an integer list
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Main driver program
while True:
    N = int(input("Please input a number: "))
    
    if N == 0:
        print("Goodbye!")
        break
    
    factors = factorize(N)
    factor_sum = sum_array(factors)
    
    print("Factor sum: %d" % factor_sum)
    
    if factor_sum == N:
        print("%d is perfect" % N)
    elif factor_sum > N:
        print("%d is abundant" % N)
    else:
        print("%d is deficient" % N)
