# Copy here code of line function from previous exercise and use it in your solution
def line(length, string):
    character = '*' 
    if(string != ''):
        character = string[0]
    print(character*length)

def shape(triHeight, triChar, rectHeight, rectChar):
    count = 1
    while count <= triHeight:
        line(count, triChar)
        count = count + 1
    while rectHeight > 0:
        line(triHeight, rectChar)
        rectHeight = rectHeight - 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")