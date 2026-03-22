import datetime
import csv

def final_points():
    start_times = {}
    best_exercises = {}
    with open('src/start_times.csv') as times, open('src/submissions.csv') as submissions:
        start_data = csv.reader(times, delimiter = ';')
        for row in start_data:
            start_times[row[0]] = datetime.datetime.strptime(row[1], '%H:%M')
    
        submission_data = csv.reader(submissions, delimiter = ';')
        
        for row in submission_data:
            name = row[0]
            if datetime.datetime.strptime(row[3], '%H:%M') - start_times[row[0]] > datetime.timedelta(hours=3):
                continue
            exercise_num = row[1]
            exercise_points = row[2]
            if name not in best_exercises:
                best_exercises[name] = {}
            if exercise_num in best_exercises[name]:
                if exercise_points > best_exercises[name][exercise_num]:
                    best_exercises[name][exercise_num] = exercise_points
            else:
                best_exercises[name][exercise_num] = exercise_points

        final_points = {}
        for name in best_exercises:
            total_points = 0
            for points in best_exercises[name].values():
                total_points += int(points)
            final_points[name] = total_points
        
        return final_points

if __name__ == '__main__':
    final_points()