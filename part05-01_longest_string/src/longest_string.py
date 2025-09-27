# Write your solution here
def longest(strings: list): 
    longest = ''
    for word in strings:
        if len(word) > len(longest):
            longest = word
    return longest