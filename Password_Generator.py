# Alex Park
# May 2021 
# Password Generator 

import string
import random

# Ask user if they want to require uppercase letters, lowercase letters, numbers, and/or symbols
def password_requirements():
    valid_upper = False
    valid_lower = False
    valid_numbers = False
    valid_symbols = False

    print("=======================================================")
    while not valid_upper:
        print("Do you want uppercase letters in your password? ")
        upper = input("Type 'Y' for yes or 'N' for no: ")
        print("")
        if upper == "Y" or upper == "y":
            upper = True
            valid_upper = True
        elif upper == "N" or upper == "n":
            upper = False
            valid_upper = True
        else: 
            print("Please enter a valid input, 'Y' (Yes) or 'N' (No).\n")
    print("=======================================================")
    while not valid_lower:
        print("Do you want lowercase letters in your password? ")
        lower = input("Type 'Y' for yes or 'N' for no: ")
        print("")
        if lower == "Y" or lower == "y":
            lower = True
            valid_lower = True
        elif lower == "N" or lower == "n":
            lower = False
            valid_lower = True
        else: 
            print("Please enter a valid input, 'Y' (Yes) or 'N' (No).\n")
    print("=======================================================")
    while not valid_numbers:
        print("Do you want numbers in your password? ")
        numbers = input("Type 'Y' for yes or 'N' for no: ")
        print("")
        if numbers == "Y" or numbers == "y":
            numbers = True
            valid_numbers = True
        elif numbers == "N" or numbers == "n":
            numbers = False
            valid_numbers = True
        else: 
            print("Please enter a valid input, 'Y' (Yes) or 'N' (No).\n")
    print("=======================================================")
    while not valid_symbols:
        print("Do you want symbols in your password? ")
        symbols = input("Type 'Y' for yes or 'N' for no: ")
        print("")
        if symbols == "Y" or symbols == "y":
            symbols = True
            valid_symbols = True
        elif symbols == "N" or symbols == "n":
            symbols = False
            valid_symbols = True
        else:
            print("Please enter a valid input, 'Y' (Yes) or 'N' (No).\n")
    return [upper, lower, numbers, symbols]

# Randomly generates a character for a spot in the password
def list_generator(requirements):
    final = []

    alphabet_upper = string.ascii_uppercase 
    alphabet_upper_list = list(alphabet_upper)

    alphabet_lower = string.ascii_lowercase 
    alphabet_lower_list = list(alphabet_lower)

    numbers = string.digits
    numbers_list = list(numbers)

    symbols = string.printable
    symbols_list = list(symbols[62:84])

    if requirements[0] == True:
        final += alphabet_upper_list
    if requirements[1] == True:
        final += alphabet_lower_list
    if requirements[2] == True:
        final += numbers_list
    if requirements[3] == True:
        final += symbols_list
    
    return final 

def random_character(criteria):
    random_spot = random.randint(0, len(criteria)-1)
    return criteria[random_spot]


# Prompts user how long they want the password to be
def length(size_check):
    valid_size = False
    while not valid_size:
        try:
            print("=======================================================")
            length = int(input("How long do you want your password to be?: "))
        except ValueError:
            print("\nLength input needs to be an integer.")
        else:
            if length > len(size_check):
                print("\nYou must make a shorter password!")
            elif length <= len(size_check):
                valid_size = True
    return length
    
# Rearranges list based on whether user wants repeats or no repeats in the password 
def repeats(password_list, criteria_list):
    valid_answer = False
    final_characters = ""
    print("=======================================================")
    print("Do you want possible character repeats in your password? ")
    answer = input("Type 'Y' for yes or 'N' for no: ")
    while not valid_answer: 
        if answer == "Y" or answer == "y":
            for each in password_list:
                final_characters += each
            valid_answer = True
            return final_characters
       
        elif answer == "N" or answer == "n":
            for each in password_list:
                if each not in final_characters:
                    final_characters += each
                elif each in final_characters:
                    replacement = random_character(criteria_list)
                    while replacement in final_characters:
                        replacement = random_character(criteria_list)
                    final_characters += replacement
            valid_answer = True
            return final_characters
        else: 
            print("Please enter a valid input, 'Y' (Yes) or 'N' (No).")
    
# Implements all methods and gives the user a password based on the criteria they want
def main():
    requirements = password_requirements()
    criteria_list = list_generator(requirements)
    password_size = length(criteria_list)
    password_list = []
    while len(password_list) < password_size:
        password_character = random_character(criteria_list)
        password_list.append(password_character)
    final_password = repeats(password_list, criteria_list)
    print("=======================================================")
    print("\nHere is your password: " + final_password)
    print("")

main()



