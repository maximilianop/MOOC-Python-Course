# Write your solution here
def anagrams(one: str, two: str) -> bool:
    oneS = sorted(one)
    twoS = sorted(two)

    if len(oneS) != len(twoS):
        return False
    for i in range(0, len(oneS)):
        if oneS[i] != twoS[i]:
            return False
    return True