# Write your solution here
def new_person(name: str, age: int):
    if len(name) > 40 or len(name) == 0 or len(name.split(" ")) < 2:
        raise ValueError(f"The name is invalid: {name}")
    if age < 0 or age > 150:
        raise ValueError(f"The age is invalid: {age}")
    
    return (name, age)