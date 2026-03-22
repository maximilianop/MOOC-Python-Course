# Write your solution here
def filter_incorrect(): 
    with open('src/lottery_numbers.csv', 'r') as lottery_numbers, open('correct_numbers.csv', 'w') as correct_numbers:
        for line in lottery_numbers:
            data = line.rstrip().split(';')
            week = data[0].split(' ')[1]
            nums = data[1].split(',')

            try:
                int(week)
                num_set = {}
                if len(nums) != 7:
                    continue
                num_set = set()
                for num in nums:
                    if int(num) in num_set:
                        raise ValueError('Duplicate number')
                    else: 
                        num_set.add(int(num))
                    if int(num) < 1 or int(num) > 39:
                        raise ValueError('Wrong size number')
                correct_numbers.write(line)
            except:
                pass


if __name__ == '__main__':
    filter_incorrect()