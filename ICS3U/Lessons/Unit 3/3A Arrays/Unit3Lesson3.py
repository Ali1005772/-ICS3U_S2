items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []

# Predict A:
# Purpose: Calculate the length of each string in the 'items' list.
# Data types: 
#   - items[i] is a string
#   - sizeI is an integer representing the length of the string
#   - sizes is a list of integers
# Output: No direct output here, just building the sizes list.
for i in range(len(items)):
    sizeI = len(items[i])
    sizes.append(sizeI)

# Predict B:
# Output: For each index, print the integer size followed by the item string.
# Expected output:
# 6 Apples
# 7 Bananas
# 8 Cherries
# 4 Dosa
for i in range(len(sizes)):
    print("%d %s" % (sizes[i], items[i]))

# Modification:
# Add a loop that compares if sizes[i] equals len(items[i]) and prints True or False
for i in range(len(items)):
    print(sizes[i] == len(items[i]))
