string_1 = input()

length = len(string_1)

lists =[]

for index in range(length):
    for key in range (index + 1, length + 1):
        flag = string_1[index:key]
        if flag ==flag[::-1]:
            lists.append(flag)

print(lists)

max_length = len(lists[0])
k = 0
for i in range (1 , len(lists)):
    if len(lists[i]) > max_length:
        max_length = len(lists[i])
        k = i
print(lists[k])
