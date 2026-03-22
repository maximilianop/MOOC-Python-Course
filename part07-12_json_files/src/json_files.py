# Write your solution here

import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
    persons = json.loads(data)
    for person in persons:
        #Peter Pythons 27 years (coding, knitting)
        print(f'{person['name']} {person['age']} years ({", ".join(person['hobbies'])})')
