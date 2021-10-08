length = int(input())

arr = list(map(int,input().split()))

sorted_arr = sorted(arr)

left = 0
right = 0

for index in range (length):
    if arr[index] != sorted_arr[index]:
        left = index
        break

for index in range (length-1 , -1 , -1):
    if arr[index] != sorted_arr[index]:
        right = index
        break

start, end = left, right

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

if arr != sorted_arr:
    print('no')
else:
    print('yes')
    print(left + 1, right + 1)
