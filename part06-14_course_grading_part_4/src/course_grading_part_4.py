def get_total_points(exercise_points: dict, exam_points: dict):
    total_points = {}
    for sid in exercise_points:
        total_points[sid] = (exercise_points[sid] // 4) + exam_points[sid]
    return total_points

def get_grades(total_points: dict):
        grades = {}
        for sid in total_points:
            if total_points[sid] >= 28:
                grades[sid] = 5
            elif total_points[sid] >= 24:
                grades[sid] = 4
            elif total_points[sid] >= 21:
                grades[sid] = 3
            elif total_points[sid] >= 18:
                grades[sid] = 2
            elif total_points[sid] >= 15:
                grades[sid] = 1
            else:
                grades[sid] = 0
        return grades

def get_course_info(course_info_file: str) -> str:
    course = []
    with open(course_info_file) as file:
        for line in file:
            course.append(line.split(':')[1].strip())
    return course

def save_results_txt(course_info_file, names, exercises, exam_points, total_points, grades):
    with open('results.txt', 'w') as results, open(course_info_file) as course_file:
        course_info = get_course_info(course_info_file)
        course_info_string = f"{course_info[0]}, {course_info[1]} credits"
        results.write(f'{course_info_string}\n')
        results.write(f'{'=' * len(course_info_string)}\n')
        results.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")
        for sid in names:
            results.write(f"{names[sid]:30}{exercises[sid]:<10}{(exercises[sid] // 4):<10}{exam_points[sid]:<10}{total_points[sid]:<10}{grades[sid]:<10}\n")

def save_results_csv(names, grades):
    with open('results.csv', 'w') as results:
        for name in names:
            results.write(f"{name};{names[name]};{grades[name]}\n")

if True:
    student_info = input('Student information: ')
    exercise_data = input('Exercises completed: ')
    exam_data = input('Exam points: ')
    course_info = input('Course information: ')
else:
    # hard-coded input
    student_info = "src/students1.csv"
    exercise_data = "src/exercises1.csv"
    exam_data = 'src/exam_points1.csv'
    course_info = 'src/course1.txt'

# dict of 'id' -> 'first_name last_name'
names = {}
with open(student_info) as file:
    for line in file:
        line = line.rstrip().split(';')
        if line[0] == 'id':
            continue
        names[line[0]] = f"{line[1]} {line[2]}"

# dict of 'id' -> total number of exercise points
exercises = {}
with open(exercise_data) as file:
    for line in file:
        line = line.split(';')
        if line[0] == 'id':
            continue
        exercises[line[0]] = 0
        for exercise in range(1, len(line)):
            exercises[line[0]] = exercises[line[0]] + int(line[exercise])

# dict of 'id' -> total number of exam points 
exam_points = {}
with open(exam_data) as file:
    for line in file:
        line = line.strip().split(';')
        if line[0] == 'id':
            continue
        exam_points[line[0]] = 0
        for i in range(1, len(line)):
            exam_points[line[0]] = exam_points[line[0]] + int(line[i])

total_points = get_total_points(exercises, exam_points)
grades = get_grades(total_points)
save_results_txt(course_info, names, exercises, exam_points, total_points, grades)
save_results_csv(names, grades)

print('Results written to files results.txt and results.csv')    