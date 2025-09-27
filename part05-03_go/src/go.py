# Write your solution here
def who_won(game_board: list):
    playerOne = 0
    playerTwo = 0
    for row in game_board:
        for value in row:
            if value == 1:
                playerOne += 1
            elif value == 2:
                playerTwo += 1
    winner = 0
    if playerOne > playerTwo:
        winner = 1
    elif playerTwo > playerOne:
        winner = 2
    return winner