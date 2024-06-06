import random
import string

def generate_password(minimum_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special_chars
    
    password = ""
    meets_criteria = False
    has_number = False
    has_special_chars = False

    while not meets_criteria or len(password) < minimum_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_chars:
            has_special_chars = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special_chars # "and" is a logical operator that returns True if both expressions at the left and right are true

    return password

generate_password(12)