# Write your solution here
from random import randint
from string import ascii_lowercase

def generate_password(num: int):
    password = ''
    for i in range(0, num):
        password += ascii_lowercase[randint(0, 25)]
    return password