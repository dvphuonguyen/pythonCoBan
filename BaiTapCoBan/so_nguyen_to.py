n = int(input("Nhap mot so nguyen bat ki: "))

flag = 1

if n >= 2:
    for index in range(2,n):
        if n % index == 0:
            flag = 0
            break
else :
    flag = 0

if flag == 1:
    print(f"{n} la so nguyen to")
else :
    print(f"{n} khong phai la so nguyen to")
