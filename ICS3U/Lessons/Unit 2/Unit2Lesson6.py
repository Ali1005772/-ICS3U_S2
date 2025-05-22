import math

# Print header
print(f"{'N':>3}|{'SQR':>5}|{'Cubes':>7}|{'Roots':>5}")
print("---+-----+-------+-----")

# Loop from 10 to 200 (inclusive) in steps of 15
for N in range(10, 201, 15):
    sqr = N ** 2
    cube = N ** 3
    root = math.sqrt(N)
    # Format and print each row with specified field widths and rounding for root
    print(f"{N:3d}|{sqr:5d}|{cube:7d}|{root:5.2f}")
