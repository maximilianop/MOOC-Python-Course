# Write your solution here

nums = []
while True:
    print(f'The list is now {nums}')
    letter = input('a(d)d, (r)emove or e(x)it: ')
    if letter == 'd':
        if len(nums) == 0:
            nums.append(1)
        else:
            nums.append(nums[-1] + 1)
    elif letter == 'r':
        nums.pop(-1)
    else:
        print('Bye!')
        break;