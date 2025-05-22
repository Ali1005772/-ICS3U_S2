# Unit 3, Exercise 2: Arrays of String: Grocery List

# Original list
items = ["Apples", "Bananas", "Cherries", "Dosa"]

# Predict A: print the list itself
print(items)
# Output: ['Apples', 'Bananas', 'Cherries', 'Dosa']

# Predict B: print number of items using % formatting
print("The number of items is %d." % len(items))
# Output: The number of items is 4.

# Predict C: print each item on its own line
for i in items:
    print(i)

# Predict D: print index and item
for c in range(len(items)):
    print(c, items[c])

print()  # Blank line to separate parts

# Modify: input from user

num_items = int(input("How many items are you entering? "))

print("Enter your items now:")

user_items = []
for _ in range(num_items):
    item = input("Next item: ")
    user_items.append(item)

# Print count without f-string
print("You have entered %d items." % len(user_items))

for item in user_items:
    print(item)
