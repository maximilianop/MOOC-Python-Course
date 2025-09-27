# Write your solution here
def line(length, string):
    character = '*' 
    if(string != ''):
        character = string[0]
    print(character*length)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")