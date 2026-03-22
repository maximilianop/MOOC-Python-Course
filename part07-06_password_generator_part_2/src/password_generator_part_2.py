# Write your solution here
from random import choice, randint
from string import ascii_lowercase, digits

def generate_strong_password(length: int, include_nums: bool, include_punc: bool):
    password = choice(ascii_lowercase)
    all_chars = ascii_lowercase

    if include_nums:
        password += choice(digits)
        all_chars += digits
    if include_punc:
        password += choice('!?=+-()#')
        all_chars += '!?=+-()#'
    
    while len(password) < length:
        password += choice(all_chars)
    return password

if __name__ == '__main__':
    generate_strong_password(8, True, True)