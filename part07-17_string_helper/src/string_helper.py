# Write your solution here
from typing import Tuple, Set

from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase
from string import digits

def change_case(orig_string: str) -> str:
    ret_string = ""
    for i in range(0, len(orig_string)):
        if orig_string[i] in lowercase:
            ret_string += uppercase[lowercase.index(orig_string[i])]
        elif orig_string[i] in uppercase:
            ret_string += lowercase[uppercase.index(orig_string[i])]
        else: 
            ret_string += orig_string[i]
    return ret_string

def split_in_half(orig_string: str) -> Tuple[str, str]:
    first_half = orig_string[0:(len(orig_string)//2)]
    second_half = orig_string[len(orig_string)//2:]
    return first_half, second_half

def remove_special_characters(orig_string: str) -> str: 
    eligible = lowercase + uppercase + digits
    eligible_chars = {i for i in eligible}
    eligible_chars.add(" ")

    ret_string = ""
    for character in orig_string:
        if character in eligible_chars:
            ret_string += character

    return ret_string

if __name__ == "__main__":
    remove_special_characters("hey!")

