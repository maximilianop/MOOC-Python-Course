# Write your solution here
def list_sum(list1: list, list2: list):
    sums = []
    for i in range(len(list1)):
        sums.append(list1[i] + list2[i])
    return sums