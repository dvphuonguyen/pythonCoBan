""" Tim tat ca cac phan tu trong ma tran
co so uoc >= 2
"""
row = int(input("Nhap so dong: "))

arrs=[]

for i in range(row):
    l = list(map(int,input().split()))
    arrs.append(l)

respond = []
total = 0
for index in range(row):
    for key in range(len(arrs[index])):
        if arrs[index][key] == 0:
            count = 2
        else:
            count = 0
            for i in range(1,arrs[index][key] + 1):
                if arrs[index][key] % i == 0:
                    count += 1
        if count >= 2:
            total += 1
            respond.append(arrs[index][key])

print(respond)
print(total)
