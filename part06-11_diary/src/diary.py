# Write your solution here
while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    user_input = int(input('Function: '))
    if user_input == 1:
        with open('diary.txt', 'a') as diary:
            entry = input('Diary entry:')
            diary.write(f'{entry}\n')
            print('Diary saved')
    elif user_input == 2:
        with open('diary.txt') as diary:
            print('Entries:')
            for line in diary:
                print(line)
    else:
        break

print('Bye now!')