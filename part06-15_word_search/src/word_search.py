# Write your solution here
def find_words(search_term: str):
    #construct list of words
    words = []
    with open('words.txt') as file:
        for word in file:
            words.append(word.strip())
    
    matching_words = []
    if '.' in search_term:
        for word in words:
            if len(word) == len(search_term):
                different = False
                for i in range(0, len(word)):
                    if search_term[i] == '.':
                        continue
                    elif search_term[i] != word[i]:
                        different = True
                        break;
                if not different:
                    matching_words.append(word)
    elif '*' in search_term:
        if search_term[0] == '*':
            for word in words:
                if word.endswith(search_term[1:]):
                    matching_words.append(word)
        else:
            for word in words:
                if word.startswith(search_term[:len(search_term)-1]):
                    matching_words.append(word)
    else:
        for word in words:
            if search_term == word:
                matching_words.append(word)
    
    return matching_words