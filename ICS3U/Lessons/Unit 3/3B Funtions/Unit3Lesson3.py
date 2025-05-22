def random(seed: float) -> float:
    modulus = 65536
    multiplier = 25173
    increment = 13849

    # Apply the LCG formula
    seed = (multiplier * seed + increment) % modulus
    
    # Return a float in [0, 1)
    return seed / modulus

def check(num, test):
    if num == test:
        return 1
    return 0

# main program
import math

one = two = three = four = five = six = seven = eight = nine = 0

for i in range(1, 10001):  # 10,000 iterations
    # Generate random number between 1 and 10 inclusive
    tendice = math.trunc(random(i) * 10 + 1)
    
    # Count occurrences for each number 1 through 9
    one += check(1, tendice)
    two += check(2, tendice)
    three += check(3, tendice)
    four += check(4, tendice)
    five += check(5, tendice)
    six += check(6, tendice)
    seven += check(7, tendice)
    eight += check(8, tendice)
    nine += check(9, tendice)

print("Frequency:")
print(" 1    2    3    4    5    6    7    8    9")
print("%4d %4d %4d %4d %4d %4d %4d %4d %4d" % (one, two, three, four, five, six, seven, eight, nine))
