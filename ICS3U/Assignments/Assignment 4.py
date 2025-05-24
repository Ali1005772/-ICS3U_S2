"""
Author: Ali Ali
Course: ICS3U
Student ID: 1005772
Last Modified: May 19, 2025
Program: Wordle Lookup Tool
Description: A tool to search Wordle solutions by word or by date.

VARIABLE DICTIONARY:
month_input      (str) : Month abbreviation entered by user (e.g., "Feb")
month_map        (dict): Maps month names to 2-digit numbers
day_input        (str) : Day entered by user
year_input       (str) : Year entered by user
numeric_date     (int) : Combined date in YYYYMMDD format
dates_list       (list): Dates from file in numeric format
words_list       (list): Wordle words from file
line_text        (str) : Current line being read from file
line_parts       (list): Components of a line split into [month, day, year, word]
search_term      (str) : Word entered for search
matched_date     (int) : Date on which a word appeared (0 if not found)
option           (str) : User's search mode: 'w' or 'd'
"""

def month_to_number(mon):
    month_map = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
        "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
        "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
    return month_map.get(mon, "00")

def build_date(day, mon, year):
    return int(year + month_to_number(mon) + day)

def load_file_data(path):
    dates_list = []
    words_list = []
    file = open(path, "r")
    for line_text in file:
        line_parts = line_text.strip().split()
        if len(line_parts) == 4:
            mon = line_parts[0]
            day = line_parts[1]
            year = line_parts[2]
            word = line_parts[3]
            full_date = build_date(day.zfill(2), mon, year)
            dates_list.append(full_date)
            words_list.append(word.upper())
    file.close()
    return dates_list, words_list

def search_by_word(word_input, words_list, dates_list):
    word_input = word_input.upper()
    for i in range(len(words_list)):
        if words_list[i] == word_input:
            return dates_list[i]
    return 0

def search_by_date(target_date, dates_list, words_list):
    for i in range(len(dates_list)):
        if dates_list[i] == target_date:
            return words_list[i]
    return None

def main():
    dates_list, words_list = load_file_data("ICS3U/Data/wordle.dat")

    print("Welcome to the Wordle Lookup Tool")

    option = input("Enter 'w' to search by word or 'd' to search by date: ").lower()

    if option == "w":
        search_term = input("Enter the word to search: ")
        matched_date = search_by_word(search_term, words_list, dates_list)
        if matched_date != 0:
            print("The word " + search_term.upper() + " appeared on " + str(matched_date) + ".")
        else:
            print(search_term.upper() + " is not in the Wordle records.")

    elif option == "d":
        year_input = input("Enter the year: ")
        month_input = input("Enter the 3-letter month (e.g., 'Jan'): ").capitalize()
        day_input = input("Enter the day: ").zfill(2)

        numeric_date = build_date(day_input, month_input, year_input)

        if numeric_date < 20210619:
            print(str(numeric_date) + " is before Wordle started. Try a later date.")
        elif numeric_date > 20240421:
            print(str(numeric_date) + " is beyond the latest available date. Try an earlier one.")
        else:
            word_result = search_by_date(numeric_date, dates_list, words_list)
            if word_result is not None:
                print("The word for " + str(numeric_date) + " was " + word_result + ".")
            else:
                print("No word found for that date.")

main()
