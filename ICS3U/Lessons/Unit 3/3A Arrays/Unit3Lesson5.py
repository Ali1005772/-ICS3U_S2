myList = [22, 16, 59, 67, 55, 84, 7, 91, 89, 48, 69, 30, 98, 28, 31]

# Initialize highest and smallest to the first element
highest = myList[0]
smallest = myList[0]
total_sum = 0

# Traverse through the list
for num in myList:
    if num > highest:
        highest = num
    if num < smallest:
        smallest = num
    total_sum += num

print("The largest number is:", highest)
print("The smallest number is:", smallest)
print("The sum is:", total_sum)
