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
        if name in phonebook:
            phonebook[name].add(number)
        else:
            phonebook[name] = {number}
        print('ok!')
    else:
        name = input('name:')
        if name in phonebook:
            for n in phonebook[name]:
                print(n)
        else:
            print('no number')