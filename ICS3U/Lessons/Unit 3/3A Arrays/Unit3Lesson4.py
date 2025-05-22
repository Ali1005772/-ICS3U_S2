ar2 = [
    [3, 4, 1, 2, 6],
    [9, 2, 3, 7, 5],
    [4, 2, 1, 0, 3]
]

# Predict A: Print each element of the 2D array row by row
for i in range(len(ar2)):
    ar3 = ar2[i]
    for j in range(len(ar3)):
        print(ar3[j], end=" ")
    print()  # New line after each row

# Predict B: Print the entire 2D array as a nested list
print(ar2)

# Modification: Calculate sums of each row and store in sums_list
sums_list = []
for i in range(len(ar2)):
    row_sum = 0
    for j in range(len(ar2[i])):
        row_sum += ar2[i][j]
    sums_list.append(row_sum)

# Print the sums as a comma-separated string
print(", ".join(str(s) for s in sums_list))
