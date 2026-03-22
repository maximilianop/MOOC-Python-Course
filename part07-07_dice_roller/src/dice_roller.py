# Write your solution here

import random

def roll(die: str):
    A = '333336'
    B = '222555'
    C = '144444'
    
    if die == 'A':
        return int(A[random.randint(0, 5)])
    elif die == 'B':
        return int(B[random.randint(0, 5)])
    else:
        return int(C[random.randint(0,5)])
 
def play(die1: str, die2: str, times: int):
    die1_wins = 0
    die2_wins = 0
    ties = 0

    for i in range(0, times):
        num1 = roll(die1)
        num2 = roll(die2)
        if num1 > num2:
            die1_wins += 1
        elif num2 > num1:
            die2_wins += 1
        else: 
            ties += 1
    return (die1_wins, die2_wins, ties)
