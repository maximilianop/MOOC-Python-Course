# Copy here code of line function from previous exercise
def line(length, string):
    character = '*' 
    if(string != ''):
        character = string[0]
    print(character*length)

def square(size, character):
    # You should call function line here with proper parameters
    length = size
    while size > 0:
        line(length, character)
        size = size - 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")