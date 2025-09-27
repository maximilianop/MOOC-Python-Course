# Write your solution here

def main():
    results = [0, 0, 0, 0, 0, 0]
    points = []
    exercises = []
    totalPoints = []
    pointsAverage = 0
    passPercentage = 0

    while True:
        nums = input('Exam points and exercises completed:')
        if nums == '':
            break
        numArr = nums.split(' ')
        points.append(int(numArr[0]))
        exercises.append(int(numArr[1]))
    
    calc_results(results, totalPoints, points, exercises)
    pointsAverage = calc_average(totalPoints)
    passPercentage = calc_pass(results)
    print_statistics(results, pointsAverage, passPercentage)

def print_statistics(results: list, pointsAverage: float, passPercentage: float):
    print('Statistics:')
    print(f'Points average:{pointsAverage: .1f}')
    print(f'Pass percentage:{passPercentage: .1f}')
    print('Grade distribution:')
    for i in range(len(results)-1, -1, -1):
        print(f' {i}: {'*' * results[i]}')

def calc_results(results: list, totalPoints: list, points: list, exercises: list):
    for i in range(0, len(points)):
        totalPoints.append(points[i] + (exercises[i] // 10))
        if points[i] < 10:
            results[0] += 1
        else:
            if totalPoints[-1] <= 14:
                results[0] += 1
            elif totalPoints[-1] <= 17:
                results[1] += 1
            elif totalPoints[-1] <= 20:
                results[2] += 1
            elif totalPoints[-1] <= 23:
                results[3] += 1
            elif totalPoints[-1] <= 27:
                results[4] += 1
            else:
                results[5] += 1
    
def calc_average(totalPoints: list):
    sum = 0
    for num in totalPoints:
        sum += num
    return sum / len(totalPoints)

def calc_pass(results: list):
    totalStudents = 0
    for num in results:
        totalStudents += num
    return ((totalStudents - results[0])/totalStudents)*100

main()