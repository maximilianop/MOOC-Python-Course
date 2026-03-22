# Write your solution here

import random

def words(n: int, beginning: str):
    matching_words = []
    with open('src/words.txt', 'r') as words:
        for line in words:
            if line.startswith(beginning):
                matching_words.append(line.rstrip())
    if not (len(matching_words) >= n):
        raise ValueError('Not enough words starting with the specified beginning.')
    
    words_list = []
    while len(words_list) < n:
        random_word = random.choice(matching_words)
        if random_word not in words_list:
            words_list.append(random_word)
    return words_list