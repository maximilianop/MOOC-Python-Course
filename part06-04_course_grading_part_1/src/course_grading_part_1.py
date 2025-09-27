# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

names = {}
with open(student_info) as file:
    for line in file:
        line = line.replace('\n', '').split(';')
        if line[0] == 'id':
            continue
        names[line[0]] = line[1] + ' ' + line[2]

nums = {}
with open(exercise_data) as file:
    for line in file:
        line = line.split(';')
        if line[0] == 'id':
            continue
        nums[line[0]] = 0
        for num in range(1, len(line)):
            nums[line[0]] = nums[line[0]] + int(line[num])

for name in names:
    print(f'{names[name]} {nums[name]}')