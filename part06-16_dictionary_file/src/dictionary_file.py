# Write your solution here
while True:
    print('1 - Add word, 2 - Search, 3 - Quit')
    function = int(input('Function: '))
    if function == 1:
        with open('dictionary.txt', 'a') as file:
            fin_word = input('The word in Finnish: ')
            eng_word = input('The word in English: ')
            file.write(f'{fin_word};{eng_word}\n')
            print('Dictionary entry added')
    elif function == 2:
        search_term = input('Search term: ')
        with open('dictionary.txt') as file:
            for line in file:
                words = line.strip().split(';')
                if search_term in words[0] or search_term in words[1]:
                    print(f'{words[0]} - {words[1]}')
    else:
        print('Bye!')
        break