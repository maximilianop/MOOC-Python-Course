# Write your solution here
num = int(input('Please type in a positive integer:'))
negNum = num * -1

for i in range(negNum, num+1, 1):
    if i != 0:
        print(i)
