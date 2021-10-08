n = int(input())
m = int(input())
x = int(input())
y = int(input())

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

i = 0
j = 0
result = []
while i < n and j < m:
    if b[j] - x > a[i] :
        i += 1
    elif b[j] + y > a[j] :
        j += 1
    elif a[i] <= b[j] + y and a[i] >= b[j] - x:
        result.append((a[i],b[j]))
        i += 1
        j += 1
    

for key in range(len(result)):
    print(result[key][0],result[key][1])
