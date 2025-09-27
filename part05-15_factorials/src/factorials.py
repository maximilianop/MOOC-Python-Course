# Write your solution here
def factorials(n: int): 
    factorials = {}
    factorials[1] = 1
    for i in range (2, n + 1):
        factorials[i] = factorials[i-1] * i
    return factorials