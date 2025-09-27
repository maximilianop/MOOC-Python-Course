# Copy here code of line function from previous exercise
def line(length, string):
    character = '*' 
    if(string != ''):
        character = string[0]
    print(character*length)

def triangle(size):
    # You should call function line here with proper parameters
    length = 1
    while length <= size:
        line(length, "#")
        length = length + 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
