"""
Author         : Ali Ali
Course code    : ICS3U
Student Number : 1005772
Revision date  : May 19, 2025
Program        : Wordle Database Search
Description    : A program that reads from a Wordle solution file and allows the user to 
                 search for a Wordle solution by date or find the date on which a 
                 specific word appeared.


VARIABLE DICTIONARY

Variable Name   Type     Purpose
-------------   ----     --------------------------------------------------------------
month           str      Stores 3-letter abbreviation of the month (e.g., "Jul")
months          dict     Maps month abbreviations to 2-digit numeric strings
mon_num         str      Stores 2-digit number of the month (e.g., "07" for July)
day             str      Day of the month (2 digits, e.g., "09")
year            str      4-digit year (e.g., "2021")
date_int        int      Merged date as an integer in format YYYYMMDD (e.g., 20210709)
dates           list     List of all dates in integer format (parallel to words)
words           list     List of all Wordle words (uppercase, parallel to dates)
file            file     File object used to read from wordle.dat
line            str      A single line from the file
parts           list     List of 4 elements split from a line: [month, day, year, word]
word            str      A Wordle word (uppercase version)
search_word     str      Word entered by user for searching
result          int      Date result from searching by word; 0 if not found
search_date     int      Integer date entered by user to find a word
choice          str      User's choice: 'w' to search by word or 'd' to search by date
"""

# Converts a 3-letter month abbreviation into a 2-digit number string
def month_to_number(month):
    months = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
        "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
        "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
    return months.get(month, "00")  # Returns "00" if the month is invalid

# Combines day, month, and year into an integer in the format YYYYMMDD
def merge(day, mon, year):
    mon_num = month_to_number(mon)        # Convert month to numeric form (e.g., "Jul" → "07")
    return int(year + mon_num + day)      # Combine year, month, and day into an integer

# Loads data from the file and stores dates and words in separate arrays
def load_data(filepath):
    dates = []                            # List to store date values (as integers)
    words = []                            # List to store corresponding Wordle words
    file = open(filepath, 'r')            # Open the data file for reading
    for line in file:                     # Read each line from the file
        parts = line.strip().split()      # Remove whitespace and split the line into parts
        if len(parts) == 4:               # Check if the line has exactly 4 elements
            mon = parts[0]                # Month (e.g., "Jul")
            day = parts[1]                # Day (e.g., "09")
            year = parts[2]               # Year (e.g., "2021")
            word = parts[3]               # The Wordle word for that date
            date_int = merge(day, mon, year)  # Convert date to integer format
            dates.append(date_int)        # Add the date to the list
            words.append(word.upper())    # Add the word (in uppercase) to the list
    file.close()                          # Close the file
    return dates, words                   # Return both lists

# Searches for a word in the list and returns its associated date if found
def isMatch(search_word, words, dates):
    search_word = search_word.upper()     # Convert input word to uppercase
    for i in range(len(words)):           # Loop through the word list
        if words[i] == search_word:       # Check if the current word matches the search
            return dates[i]               # Return the date if found
    return 0                              # Return 0 if word not found

# Searches for the word that appears on a specific date
def find_word_by_date(search_date, dates, words):
    for i in range(len(dates)):           # Loop through the date list
        if dates[i] == search_date:       # Check if the current date matches the search
            return words[i]               # Return the word if date matches
    return None                           # Return None if the date is not found

# Main program logic and user interface
def main():
    # Load the data file into two lists
    dates, words = load_data("/workspaces/-ICS3U_S2/Data/wordle.dat")

    # Welcome message
    print("Welcome to the Wordle Database!")

    # Ask user if they want to search by word or date
    choice = input("Enter w if you are looking for a word, or d for a word on a certain date: ").lower()

    if choice == 'w':  # If searching by word
        word = input("What word are you looking for? ")  # Ask for the word
        result = isMatch(word, words, dates)             # Call isMatch to find the word
        if result != 0:  # If the word was found
            print("The word " + word.upper() + " was the solution to the puzzle on " + str(result))
        else:  # Word not found
            print(word.upper() + " was not found in the database.")

    elif choice == 'd':  # If searching by date
        year = input("Enter the year: ")  # Get year from user
        month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")  # Get month
        day = input("Enter the day: ")    # Get day from user

        day = day.zfill(2)  # Make sure day is 2 digits (e.g., "1" becomes "01")
        date = merge(day, month, year)  # Convert input date to integer format

        # Check if the date is within valid Wordle history
        if date < 20210619:
            print(str(date) + " is too early. No wordles occurred before 20210619. Enter a later date.")
        elif date > 20240421:
            print(str(date) + " is too recent. Our records only go as late as 20240421. Please enter an earlier date.")
        else:
            word = find_word_by_date(date, dates, words)  # Find the word for that date
            if word is not None:
                print("The word entered on " + str(date) + " was " + word + ".")
            else:
                print("No word found for that date.")

# Call the main function to run the program
main()
