n = int(input())
arr = map(int, input().split())

arr = list(set(list(arr)))
#print (arr)
arr = sorted(arr)[::-1]
#print(arr)

print(arr[1])
