''' tong cac gia tri tren duong cheo chinh'''

row = int(input("Nhap so dong = cot: "))

arr= []

for index in range(row):
    l = list(map(int,input().split()))
    arr.append(l)

total = 0
for index in range (row):
    total += arr[index][index]

print(total)
