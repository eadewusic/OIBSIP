import random
import string

def generate_password(minimum_lenth, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    print(letters, digits, special_chars)

generate_password(12)