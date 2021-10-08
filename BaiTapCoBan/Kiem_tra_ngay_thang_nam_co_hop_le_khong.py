ngay = int(input("Nhap ngay:"))

thang = int(input("Nhap thang:"))

nam = int(input("Nhap nam:"))

if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    if thang == 2 and ngay <= 29:
        print("Co ton tai")
    elif thang == 2 and ngay <= 28:
        print("Co ton tai")
elif (thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12) and ngay <=31:
    print("Co ton tai")
elif (thang == 4 or thang == 6 or thang ==9 or thang == 11) and ngay <= 30:
    print("Co ton tai")
else :
    print("Khong ton tai")

        
