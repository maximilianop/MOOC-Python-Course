# Write your solution here
from string import *
def separate_characters(my_string: str):
    letter = ''
    punc = ''
    other = ''

    for char in my_string:
        if char in ascii_letters:
            letter += char
        elif char in punctuation:
            punc += char
        else:
            other += char
    
    return (letter, punc, other)

if __name__ == '__main__':
    print(separate_characters('Olé!!! Hey, are ümläüts wörking?'))
    