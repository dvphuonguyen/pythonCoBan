lists = list(map(int,input().split()))
print(lists)

arr = list(map(int,input().split()))
arr.sort()
print(arr)

a = lists [1]
total = 0
for element in arr:
    total += (a * element)
    a -= 1
    if a < 0:
        a =0

print(total)
