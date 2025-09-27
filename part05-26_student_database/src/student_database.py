# Write your solution here
def add_student(students: dict, name: str):
    courseList = []
    students[name] = courseList

def print_student(students: dict, name: str):
    if not name in students:
        print(f'{name}: no such person in the database')
    else:
        print(f'{name}:')
        if len(students[name]) == 0:
            print(f' no completed courses')
        else:
            print(f' {len(students[name])} completed courses:')
            summation = 0
            for course in students[name]:
                summation += course[1]
                print(f'  {course[0]} {course[1]}')
            print(f' average grade {summation/len(students[name])}')

def add_course(students: dict, name: str, courseInfo):
    if (not name in students) or (courseInfo[1] == 0):
        return
    coursePresent = False
    for i in range(0, len(students[name])):
        if courseInfo[0] == students[name][i][0]:
            coursePresent = True
            if courseInfo[1] > students[name][i][1]:
                students[name][i] = courseInfo
    if not coursePresent:
        students[name].append(courseInfo)

def summary(students: dict):
    mostCoursesTuple = ('name', 0)
    bestAverageGrade = ('name', 0)
    for student in students:
        if len(students[student]) > mostCoursesTuple[1]:
            mostCoursesTuple = (student, len(students[student]))
    for student in students:
        summation = 0
        for course in students[student]:
            summation += course[1]
        if summation/len(students[student]) > bestAverageGrade[1]:
            bestAverageGrade = (student, summation/len(students[student]))
    print(f'students {len(students)}')
    print(f'most courses completed {mostCoursesTuple[1]} {mostCoursesTuple[0]}')
    print(f'best average grade {bestAverageGrade[1]} {bestAverageGrade[0]}')

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
