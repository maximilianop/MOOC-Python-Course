# Write your solution here
def get_times_and_ingredients(filename: str) -> tuple:
    file_list = []
    
    with open(filename) as file:
        i = 0
        file_list.append([])
        for line in file:
            if line != '\n':
                file_list[i].append(line.strip())
            else:
                i += 1
                file_list.append([])
    
    recipe_times = {}
    recipe_ingredients = {}

    for recipe in file_list:
        recipe_times[recipe[0]] = int(recipe[1])
        recipe_ingredients[recipe[0]] = recipe[2:]
    
    return (recipe_times, recipe_ingredients)

def search_by_name(filename: str, word: str):
    data = get_times_and_ingredients(filename)
    recipe_times = data[0]
    names = []
    for recipe_name in recipe_times:
        if word.lower() in recipe_name.lower():
            names.append(recipe_name)
    return names

def search_by_time(filename: str, prep_time: int):
    data = get_times_and_ingredients(filename)
    recipe_times = data[0]
    times = []
    for recipe in recipe_times:
        if recipe_times[recipe] <= prep_time:
            times.append(f'{recipe}, preparation time {recipe_times[recipe]} min')
    return times
    
def search_by_ingredient(filename: str, ingredient: str):
    data = get_times_and_ingredients(filename)
    recipe_times = data[0]
    recipe_ingredients = data[1]
    return_list = []
    for recipe, ingredients in recipe_ingredients.items():
        if ingredient in ingredients:
            return_list.append(f'{recipe}, preparation time {recipe_times[recipe]} min')
    return return_list

if __name__ == "__main__":
    search_by_ingredient('recipes1.txt', 'eggs')    