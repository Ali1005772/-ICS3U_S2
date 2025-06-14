"""
Author: Ali Ali
Course: ICS3U
Student ID: 1005772
Last Modified: June 14, 2025
Program: Credit Card Expiry Report

Description:
This program checks all customer credit cards from a file and sees which ones are expired
or about to expire by June 2025. It uses the Luhn algorithm to make sure the card numbers
are real, and then sorts them by date using merge sort. Finally, it shows the report in the terminal.

VARIABLE DICTIONARY:
EXPIRY_CUTOFF     (int)   : Cutoff date to check for expired cards (YYYYMM format)
INPUT_FILE        (str)   : File location of the customer credit card list
filtered_data     (list)  : Cards that passed Luhn and are expired or almost expired
fields            (list)  : Split parts of each line (first name, last name, etc.)
first             (str)   : First name of customer
last              (str)   : Last name of customer
cc_type           (str)   : Type of card (Visa or MasterCard)
cc_number         (str)   : 16-digit card number
month             (int)   : Expiry month of the card
year              (int)   : Expiry year of the card
yyyymm            (int)   : Month and year combined to sort easier
sorted_data       (list)  : List of valid expired cards, sorted by date
entry             (list)  : A single card entry from the list
name              (str)   : Full name of the customer (first + last)
status            (str)   : Shows if it's expired or needs to be renewed soon
"""

EXPIRY_CUTOFF = 202506  # This is the cutoff (June 2025)
INPUT_FILE = "/workspaces/-ICS3U_S2/ICS3U/Data/data.dat"  # Where the credit card info is stored

# Variable Dictionary for is_valid_luhn():
# total           (int) : Sum total used in Luhn calculation
# reverse_digits  (str) : Reversed string of card number for processing
# n               (int) : Single digit being processed
def is_valid_luhn(card_number):
    total = 0  # Total for the math
    reverse_digits = card_number[::-1]  # We have to start from the end
    for i in range(len(reverse_digits)):
        n = int(reverse_digits[i])  # Convert character to number
        if i % 2 == 1:  # Double every 2nd digit
            n *= 2
            if n > 9:
                n -= 9  # Subtract 9 if it’s 2 digits
        total += n  # Add to total
    return total % 10 == 0  # Valid if it ends in 0

# Variable Dictionary for merge_sort() and merge():
# data   (list): List of card entries to sort
# mid    (int) : Middle index to split list
# left   (list): Left half of the list
# right  (list): Right half of the list
# result (list): Merged and sorted list
# i, j   (int) : Index counters for left and right halves
def merge_sort(data):
    if len(data) <= 1:
        return data  # If only one item, already sorted
    mid = len(data) // 2
    left = merge_sort(data[:mid])   # Sort the first half
    right = merge_sort(data[mid:])  # Sort the second half
    return merge(left, right)       # Merge both halves

def merge(left, right):
    result = []  # Final sorted list
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][4] <= right[j][4]:  # Compare expiry dates
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])  # Add what's left in left half
    result.extend(right[j:]) # Add what's left in right half
    return result

# MAIN PROGRAM STARTS HERE
try:
    filtered_data = []  # Store all the cards we need to warn

    with open(INPUT_FILE, 'r') as file:
        lines = file.readlines()[1:]  # Skip the first line (the header)

        for line in lines:
            fields = line.strip().split(',')  # Split line into pieces
            first = fields[0]        # First name
            last = fields[1]         # Last name
            cc_type = fields[2]      # Visa or MasterCard
            cc_number = fields[3]    # Credit card number
            month = int(fields[4])   # Expiry month
            year = int(fields[5])    # Expiry year

            # Make expiry date into one number like 202504
            if month < 10:
                yyyymm = int(str(year) + '0' + str(month))
            else:
                yyyymm = int(str(year) + str(month))

            # Only use cards that are valid AND need to be renewed
            if is_valid_luhn(cc_number) and yyyymm <= EXPIRY_CUTOFF:
                filtered_data.append([first, last, cc_type, cc_number, yyyymm])

    # Sort the valid expired cards by date
    sorted_data = merge_sort(filtered_data)

    # Show the report in the terminal
    for entry in sorted_data:
        name = entry[0] + " " + entry[1]  # Get full name
        cc_type = entry[2]
        cc_number = "#" + entry[3]
        yyyymm = entry[4]
        if yyyymm < EXPIRY_CUTOFF:
            status = "EXPIRED"
        else:
            status = "RENEW IMMEDIATELY"

        # Print the final output in nice format
        print("{:<20} {:<12} {:<20} {} {}".format(name, cc_type, cc_number, yyyymm, status))

# If the file is missing, show error
except FileNotFoundError:
    print("❌ Error: Input file not found.")

# Catch anything else that might go wrong
except Exception as e:
    print("❌ An error occurred: " + str(e))
