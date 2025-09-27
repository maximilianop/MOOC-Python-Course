# write your solution here
words = []
with open('wordlist.txt') as file:
    for line in file:
        words.append(line.strip())

user_input = input('Write text:')
user_input = user_input.split(' ')
for i in range(0, len(user_input)):
    if not user_input[i].lower() in words:
        user_input[i] = f'*{user_input[i]}*'

print(' '.join(user_input))
        

        