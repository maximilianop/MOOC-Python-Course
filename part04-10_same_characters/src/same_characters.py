# Write your solution here
def same_chars(value, indexOne, indexTwo):
    if len(value) == 0 or indexOne >= len(value) or indexTwo >= len(value):
        return False
    elif value[indexOne] == value[indexTwo]:
        return True
    return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))