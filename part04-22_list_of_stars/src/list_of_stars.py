# Write your solution here
def list_of_stars(argList: list):
    for num in argList:
        stars = '*' * num
        print(stars)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2]
    result = list_of_stars(my_list)
    print(result)