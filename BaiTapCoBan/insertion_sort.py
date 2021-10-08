arr = list(map(int,input().split(' ')))

print (arr)

length = len(arr)

if length <= 1:
    print('Mang theo thu tu')
else :
    for index in range (1, len(arr)):
        key = arr[index]
        now = index - 1
        while now >= 0 and arr[now] > key:
            arr[now + 1] = arr[now]
            now -= 1
        arr[now + 1] = key

print (arr)
