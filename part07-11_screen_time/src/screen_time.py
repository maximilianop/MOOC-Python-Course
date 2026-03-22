# Write your solution here
import datetime

def get_total_mins(usage_map: dict):
    total_mins = 0
    for date in usage_map:
        for minutes in usage_map[date]:
            total_mins += int(minutes)
    return total_mins

def get_average_mins(usage_map: dict):
    return get_total_mins(usage_map) / len(usage_map)

file_name = input('Filename: ')
start_date = datetime.datetime.strptime(input('Starting date: '), '%d.%m.%Y')
num_days = int(input('How many days: '))

usage_map = {}

for i in range(0, num_days):
    curr_date = (start_date +  datetime.timedelta(days=i)).strftime('%d.%m.%Y')
    screen_time = input(f'Screen time {curr_date}: ').split(" ")
    usage_map[curr_date] = screen_time

with open(file_name, 'w') as usage_file:
    usage_file.write(f'Time period: {start_date.strftime('%d.%m.%Y')}-{(start_date + datetime.timedelta(days=num_days-1)).strftime('%d.%m.%Y')}\n')
    usage_file.write(f'Total minutes: {get_total_mins(usage_map)}\n')
    usage_file.write(f'Average minutes: {get_average_mins(usage_map)}\n')
    for date in usage_map:
        usage_file.write(f'{date}: {'/'.join(usage_map[date])}\n')
