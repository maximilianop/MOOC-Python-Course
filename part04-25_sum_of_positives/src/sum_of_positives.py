# Write your solution here
def sum_of_positives(ints: list) -> int:
    sum = 0
    for i in ints:
        if i > 0:
            sum = sum + i
    return sum