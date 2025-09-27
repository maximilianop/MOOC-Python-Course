# Write your solution here
def no_vowels(myString: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in vowels:
        myString = myString.replace(char, '')
    return myString