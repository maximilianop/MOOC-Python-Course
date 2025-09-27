# Write your solution here
def palindromes(word: str):
    for i in range(0, len(word)):
        if word[i] != word[-i - 1]:
            return False
    return True

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def main():
    while True:
        word = input('Please type in a palindrome:')
        if palindromes(word):
            print(f'{word} is a palindrome!')
            break
        else:
            print('that wasn\'t a palindrome')

main()