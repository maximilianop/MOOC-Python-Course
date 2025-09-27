# Write your solution here
nums = []
while True:
    num = int(input('New Item:'))
    if num == 0:
        print('Bye!')
        break
    nums.append(num)
    print(f'The list now: {nums}')
    print(f'The list in order: {sorted(nums)}')