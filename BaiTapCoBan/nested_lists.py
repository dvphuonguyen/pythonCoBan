import math
if __name__ == '__main__':
    a = [None]*2
    lists = []
    numbers = int(input())
    for index in range(numbers):
        name = input()
        score = float(input())
        a = [score, name]
        lists.append(a)
    print(lists)
    arr = sorted(lists)
    print(arr)
    c = arr[0][0]
    index = 0
    while index < len(arr):
        if c == arr[index][0]:
            arr.pop(0)
        else :
            index += 1
    print(arr)

    b = arr[0][0]
    for i in range(len(arr)):
        if b == arr[i][0]:
            print(arr[i][1])
      

