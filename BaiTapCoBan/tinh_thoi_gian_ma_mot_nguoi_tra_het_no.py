loan = float(input("Tien cho vay: "))

thang = 0
if loan != 10:
    while loan > 0:
        if thang != 0:
            loan = loan*1.01 - 10
            thang +=1
        else:
            loan -= 10
            thang += 1
    print("Sau",thang,"thang thi nguoi do tra het no")
else:
    print("Sau 1 thang thi nguoi do tra het no")
