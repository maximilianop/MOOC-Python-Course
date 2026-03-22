# Write your solution here
def read_input(text, num_1, num_2):
    while True:
        try:
            num = int(input(text))
            if num >= num_1 and num <= num_2:
                return num
        except:
            pass
        print(f'You must type in an integer between {num_1} and {num_2}')


if __name__ == '__main__':
    read_input('Enter a number', 5, 10)