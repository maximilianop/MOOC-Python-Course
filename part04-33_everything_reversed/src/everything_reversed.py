# Write your solution here
def everything_reversed(strings: list): 
    reversed = []
    for word in strings[::-1]:
        reversed.append(word[::-1])
    return reversed