# Write your solution here
def no_shouting(words: list):
    newWords = []
    for word in words:
        if not word.isupper():
            newWords.append(word)
    return newWords
        