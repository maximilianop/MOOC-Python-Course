# write your solution here
def largest() -> int:
    with open('numbers.txt') as nums_file:
        largest = 0
        for line in nums_file:
            line = line.replace('\n', '')
            num = int(line)
            if num > largest:
                largest = num
        return largest
