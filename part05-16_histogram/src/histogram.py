# Write your solution here
def histogram(word: str):
    histogram = {}
    for letter in word:
        if letter in histogram:
            histogram[letter] = histogram[letter] + 1
        else:
            histogram[letter] = 1
    for key, value in histogram.items():
        print(f'{key} {'*' * value}')