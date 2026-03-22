# Write your solution here
import datetime

def cheaters():
    start_times = {}
    cheaters = []
    with open('src/start_times.csv') as file1:
        for line in file1:
            data = line.rstrip().split(';')
            start_times[data[0]] = datetime.datetime.strptime(data[1], '%H:%M')
    
    with open('src/submissions.csv') as file2:
        for line in file2:
            submission_data = line.rstrip().split(';')
            student_start_time = start_times[submission_data[0]]
            if datetime.datetime.strptime(submission_data[3], '%H:%M') - student_start_time > datetime.timedelta(hours=3):
                if submission_data[0] not in cheaters:
                    cheaters.append(submission_data[0])
    
    return cheaters

if __name__ == '__main__':
    cheaters()