# Write your solution here
def invert(dictionary: dict):
    newDict = {}
    for key in dictionary:
        value = dictionary[key]
        newDict[value] = key
    dictionary.clear()
    for key in newDict:
        dictionary[key] = newDict[key]

if __name__ == "__main__":
    dictionary = {}
    dictionary[1] = 100
    invert(dictionary)
        