# Write your solution here
def all_the_longest(myList: list):
    longest = []
    length = 0
    for word in myList:
        if len(word) > length:
            length = len(word)
    
    for word in myList:
        if len(word) == length:
            longest.append(word)
    
    return longest