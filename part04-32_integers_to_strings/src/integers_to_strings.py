# Write your solution here
def formatted(nums: list):
    formattedNums = []
    for num in nums:
        formattedNums.append(f'{num:.2f}')
    return formattedNums