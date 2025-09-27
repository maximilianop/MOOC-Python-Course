# Write your solution here
# open both files and clear them
# go through solutions and separate incorrect operations and correct operations into two two arrays
# write the incorrect ones and correct ones to the two files
# two helper functions
#   one to determine correctness
#   one to write to the files

def is_correct(equation: list) -> bool:
    # [Arto, 2+5, 7]
    if '+' in equation[1]:
        operands = equation[1].split('+')
        return int(equation[2]) == int(operands[0]) + int(operands[1])
    else:
        operands = equation[1].split('-')
        return int(equation[2]) == int(operands[0]) - int(operands[1])

def filter_solutions():
    with open ('src/solutions.csv') as solutions, open('correct.csv', 'w') as correct_file, open('incorrect.csv', 'w') as incorrect_file:
        for line in solutions:
            entry = line.rstrip().split(';')
            result = is_correct(entry)
            if result:
                correct_file.write(line)
            else:
                incorrect_file.write(line)

if __name__ == "__main__":
    filter_solutions()