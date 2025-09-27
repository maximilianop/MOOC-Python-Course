# write your solution here
def read_fruits() -> dict:
    with open("fruits.csv") as fruits_file:
        fruit_dict = {}
        for line in fruits_file:
            arr = line.split(';')
            fruit_dict[arr[0]] = float(arr[1])
        return fruit_dict

if __name__ == "__main__":
    read_fruits()