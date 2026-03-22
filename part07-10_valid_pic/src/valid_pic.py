# Write your solution here
from datetime import datetime

def is_it_valid(pic: str): 
    day = pic[0:2]
    month = pic[2:4]
    year = pic[4:6]
    century = pic[6]
    identifier = pic[7:10]
    control = pic[10]

    if len(pic) != 11:
        return False
    if int(day) > 31 or int(day) < 0:
        return False
    if int(month) < 1 or int(month) > 12:
        return False 
    try: 
        if century == '+':
            birthday = datetime((1800+int(year)), int(month), int(day))
        elif century == '-':
            birthday = datetime((1900+int(year)), int(month), int(day))
        elif century == 'A':
            birthday = datetime((2000+int(year)), int(month), int(day))
        else:
            return False
    except:
        return False
    
    if birthday >= datetime.now():
        return False

    valid_controls = '0123456789ABCDEFHJKLMNPRSTUVWXY'

    whole_string = day + month + year + identifier
    result = int(whole_string) % 31
    if control != valid_controls[result]:
        return False
    
    return True

if __name__ == '__main__':
    is_it_valid('310286+713J')