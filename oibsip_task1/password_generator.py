import random
import string

def generate_password(minimum_length, numbers=True, special_characters=True):
    letters = string.ascii_letters #contains all lowercase and uppercase letters
    digits = string.digits #contains 0-9 as digit characters in form of string and not actual numerical value which why we can concatenate
    special_chars = string.punctuation

    characters = letters #created the variable 'characters' that holds the string from another variable 'letters' which contains all the different characters we could be selecting from (('cus we've added other characters - digits & special_chars through string concatenation. So, characters includes more characters now)
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