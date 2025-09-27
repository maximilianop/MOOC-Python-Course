# Write your solution here
def create_tuple(x: int, y: int, z: int): 
    maxNum = max(x, y, z)
    minNum = min(x, y, z)
    summation = x + y + z

    return (minNum, maxNum, summation)
