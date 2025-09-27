# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    matches = 0
    for row in my_matrix:
        for num in row:
            if num == element:
                matches += 1
    return matches
