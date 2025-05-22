def read_magic_square(filename):
    with open(filename, "r") as fh:
        dim = int(fh.readline().strip())
        magicSq = []
        for _ in range(dim):
            row = fh.readline().strip().split()
            magicSq.append(row)
    return dim, magicSq

def is_magic_square(dim, square):
    # Convert all entries to integers
    for i in range(dim):
        for j in range(dim):
            square[i][j] = int(square[i][j])
    
    # Check that all numbers from 1 to dim^2 are present exactly once
    nums = [square[i][j] for i in range(dim) for j in range(dim)]
    if sorted(nums) != list(range(1, dim*dim + 1)):
        print("Numbers do not form a complete set from 1 to " + str(dim*dim))
        return False
    
    # Calculate the magic sum from first row
    magic_sum = sum(square[0])
    
    # Check rows sum
    for i in range(dim):
        row_sum = sum(square[i])
        if row_sum != magic_sum:
            print("Row " + str(i) + " does not sum to " + str(magic_sum) + " (sums to " + str(row_sum) + ")")
            return False
    
    # Check columns sum
    for j in range(dim):
        col_sum = sum(square[i][j] for i in range(dim))
        if col_sum != magic_sum:
            print("Column " + str(j) + " does not sum to " + str(magic_sum) + " (sums to " + str(col_sum) + ")")
            return False
    
    # Check diagonals sum
    diag1_sum = sum(square[i][i] for i in range(dim))
    diag2_sum = sum(square[i][dim - 1 - i] for i in range(dim))
    
    if diag1_sum != magic_sum:
        print("Primary diagonal does not sum to " + str(magic_sum) + " (sums to " + str(diag1_sum) + ")")
        return False
    if diag2_sum != magic_sum:
        print("Secondary diagonal does not sum to " + str(magic_sum) + " (sums to " + str(diag2_sum) + ")")
        return False
    
    # If all checks passed
    return True

def main():
    filename = "magic.dat"  # Make sure this file exists with your magic square data
    dim, square = read_magic_square(filename)
    print("Checking a " + str(dim) + "x" + str(dim) + " square:")
    for row in square:
        print(" ".join(row))
    if is_magic_square(dim, square):
        print("This is a magic square!")
    else:
        print("This is NOT a magic square.")

if __name__ == "__main__":
    main()
