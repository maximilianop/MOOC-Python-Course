# write your solution here
def matrix_sum():
    with open("matrix.txt") as matrix:
        total = 0
        sums = row_sums()
        for num in sums:
            total += num
        return total

def matrix_max():
    with open('matrix.txt') as matrix:
        max = 0
        for line in matrix:
            nums = line.replace('\n', '').split(',')
            for num in nums:
                if int(num) > max:
                    max = int(num)
        return max

def row_sums():
    with open("matrix.txt") as matrix:
        sums = []
        for line in matrix:
            nums = line.replace('\n', '')
            nums = nums.split(',')
            total = 0
            for num in nums:
                total += int(num)
            sums.append(total)
        return sums

if __name__ == "__main__":
    row_sums()
    matrix_sum()

