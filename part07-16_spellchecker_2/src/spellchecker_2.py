# Write your solution here
import difflib

dictionary = []
with open('wordlist.txt') as words:
    for line in words:
        dictionary.append(line.rstrip())

text = input('write text: ').split(' ')
suggestions = {}

for i in range(0, len(text)):
    if text[i].lower() not in dictionary:
        suggestions[text[i]] = difflib.get_close_matches(text[i], dictionary)
        text[i] = f'*{text[i]}*'

print(' '.join(text))
print('suggestions:')
for word in suggestions:
    print(f'{word}: {', '.join(suggestions[word])}')

