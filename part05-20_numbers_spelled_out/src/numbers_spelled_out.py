# Write your solution here
def dict_of_numbers():
    dictionary = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

    for i in range(20, 100):
        key = ''
        if i // 10 == 2:
            key = 'twenty'
        elif i // 10 == 3:
            key = 'thirty'
        elif i // 10 == 4:
            key = 'forty'
        elif i // 10 == 5:
            key = 'fifty'
        elif i // 10 == 6:
            key = 'sixty'
        elif i // 10 == 7:
            key = 'seventy'
        elif i // 10 == 8:
            key = 'eighty'
        else:
            key = 'ninety'
        
        if i % 10 != 0:
            key += '-' + dictionary[i % 10]
        dictionary[i] = key
    return dictionary

if __name__ == "__main__":
    dictionary = dict_of_numbers()
    print('done')