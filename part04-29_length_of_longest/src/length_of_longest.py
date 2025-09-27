# Write your solution here
def length_of_longest(list1: list):
    length = 0
    for word in list1:
        if len(word) > length:
            length = len(word)
    return length