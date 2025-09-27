# Write your solution here
items = []
numItems = int(input('How many items:'))

count = 1
while count <= numItems:
    items.append(int(input(f'Item {count}:')))
    count = count + 1
print(items)