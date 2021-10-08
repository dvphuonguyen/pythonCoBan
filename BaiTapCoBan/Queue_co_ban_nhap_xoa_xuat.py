number = int(input())
lists = []
for index in range (number):
    current = input().split(' ')
    key = int(current[0])
    if key == 1:
        values = int(current[1])
        lists.append(values)
    elif key == 2:
        if len(lists) != 0:
            lists.pop(0)
    elif key == 3:
        if len(lists) != 0:
            print(lists[0])
