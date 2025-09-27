# wwite your solution here
# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input('Exam points:')

else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = 'exam_points1.csv'

names = {}
with open(student_info) as file:
    for line in file:
        line = line.rstrip().split(';')
        if line[0] == 'id':
            continue
        names[line[0]] = f"{line[1]} {line[2]}"

nums = {}
with open(exercise_data) as file:
    for line in file:
        line = line.split(';')
        if line[0] == 'id':
            continue
        nums[line[0]] = 0
        for num in range(1, len(line)):
            nums[line[0]] = nums[line[0]] + int(line[num])

exam_points = {}
with open(exam_data) as file:
    for line in file:
        line = line.strip().split(';')
        if line[0] == 'id':
            continue
        exam_points[line[0]] = 0
        for i in range(1, len(line)):
            exam_points[line[0]] = exam_points[line[0]] + int(line[i])

for sid in names:
    
    
    total_points = (nums[sid] // 4) + exam_points[sid]
    grade = 0

    if total_points >= 28:
        grade = 5
    elif total_points >= 24:
        grade = 4
    elif total_points >= 21:
        grade = 3
    elif total_points >= 18:
        grade = 2
    elif total_points >= 15:
        grade = 1
    else:
        grade = 0

    print(f'{names[sid]} {grade}')