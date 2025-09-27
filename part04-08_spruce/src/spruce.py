# Write your solution here
def spruce(size):
    print('a spruce!')
    count = 1
    base = size * 2 - 1
    while count <= size:
        space = ' ' * (size - count)
        chars = '*' * (base - (len(space) * 2))
        print(space+chars+space)
        count = count + 1
    space = ' ' * (size - 1)
    print(space + '*' + space)
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)