# Write your solution here
def most_common_character(my_string: str):
    char = ''
    amount = 0
    for index in my_string:
        ocur = my_string.count(index)
        if ocur > amount:
            amount = ocur
            char = index
    return char
