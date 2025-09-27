# Write your solution here
def even_numbers(nums: list):
    newNums = []
    for num in nums:
        if num % 2 == 0:
            newNums.append(num)
    return newNums