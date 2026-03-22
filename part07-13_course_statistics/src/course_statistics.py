# Write your solution here
import urllib.request
import json

def retrieve_all():
    course_data = json.load(urllib.request.urlopen('https://studies.cs.helsinki.fi/stats-mock/api/courses'))
    active_courses = []
    for course in course_data:
        if course['enabled']:
            active_courses.append((course['fullName'], course['name'], course['year'], sum(course['exercises'])))
    return active_courses

def retrieve_course(course_name: str):
    course_data = json.load(urllib.request.urlopen(f'https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats'))
    course_stats = {}
    course_stats['weeks'] = len(course_data)
    course_stats['students'] = 0
    course_stats['hours'] = 0
    course_stats['exercises'] = 0
    for val in course_data.values():
        course_stats['students'] = val['students'] if val['students'] > course_stats['students'] else course_stats['students']
        course_stats['hours'] += val['hour_total']
        course_stats['exercises'] += val['exercise_total']
    course_stats['hours_average'] = course_stats['hours'] // course_stats['students']
    course_stats['exercises_average'] = course_stats['exercises'] // course_stats['students']

    return course_stats

if __name__ == '__main__':
    retrieve_course('docker2019')
