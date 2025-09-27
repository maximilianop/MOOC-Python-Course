# Write your solution here
def find_movies(database: list, search_term: str):
    newList = []
    for movie in database:
        if search_term.lower() in movie['name'].lower():
            newList.append(movie)

    return newList