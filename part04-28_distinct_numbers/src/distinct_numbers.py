# Write your solution here
def distinct_numbers(list1: list):
    nums = []
    for num in list1:
        if num not in nums:
            nums.append(num)
    return sorted(nums)