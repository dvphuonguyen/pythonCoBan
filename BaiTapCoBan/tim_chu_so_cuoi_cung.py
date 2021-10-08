'''Hôm nay là ngày nghỉ,
Ben cùng chơi một trò chơi với các bạn của mình.
Luật trò chơi rất đơn giản,
mỗi người sẽ nhận được một con số nguyên dươnggồm có 5 chữ số.
Nếu ai có số nút từ con số này là lớn nhất thì chiến thắng.
Hãy giúp Ben tính xem số nút của con số mình nhận được là bao nhiêu.
Số nút của một con số là chữ số cuối cùng của tổng các chữ số của con số đó.
Ví dụ số 12345 có tổng của các chữ số là 1 + 2 + 3 + 4 + 5 = 15,
vậy số nút của nó là chữ số cuối cùng của 15 là con số 5'''
first = int(input("Nhap chu so thu nhat : "))

second = int(input("Nhap chu so thu hai : "))

third = int(input("Nhap chu so thu ba : "))

fourth = int(input("Nhap chu so thu tu : "))

fifth = int(input("Nhap chu so thu nam : "))

total = first + second + third + fourth + fifth

print("Chu so cuoi cung cua {total} la: ", total % 10)
