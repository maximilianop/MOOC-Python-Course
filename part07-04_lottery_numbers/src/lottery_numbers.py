# Write your solution here
from random import sample
def lottery_numbers(amount: int, lower: int, upper: int):
    num_list = sample(range(lower, upper+1), amount)
    num_list.sort()
    return num_list

if __name__ == '__main__':
    lottery_numbers(1, 1, 10)