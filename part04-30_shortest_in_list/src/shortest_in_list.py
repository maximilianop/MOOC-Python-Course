# Write your solution here
def shortest(list1: list):
    shortest = list1[0]
    for i in range(1, len(list1)):
        if len(list1[i]) < len(shortest):
            shortest = list1[i]
    return shortest