number = int(input("Nhap so nguyen bat ki: "))

if number <2:
    print(f"Khong ton tai so nguyen to gan nhat ma be hon {number}")
else:
    for index in range (number - 1, 2, -1):   
        flag = 1
        for key in range(2, index):
            if index % key == 0:
                flag = 0
                break
        if flag == 1:
            print(f"{index} la so nguyen to be hon {number} va gan {number} nhat")
            break
        
number_1 = number
while True:
        number_1 = number_1 + 1
        flag = 1
        for element in range (2, number_1):
            if number_1 % element ==0:
                flag = 0
                break
        if flag == 1:
            print(f"{number_1} la so nguyen to lon hon {number} va gan {number} nhat")
            break
        
