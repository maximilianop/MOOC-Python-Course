# Write your solution here
phonebook = {}
while (True):
    num = int(input('command (1 search, 2 add, 3 quit):' ))
    if num == 3:
        print('quitting...')
        break
    elif num == 2:
        name = input('name:')
        number = input('number:')
        phonebook[name] = number
        print('ok!')
    else:
        name = input('name:')
        if name in phonebook:
            print(f'{phonebook[name]}')
        else:
            print('no number')
