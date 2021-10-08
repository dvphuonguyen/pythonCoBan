''' nhap ho va ten sau do xuat ra'''
first_name = input("Nhap ten cua ban: ")
last_name = input("Nhap ho cua ban: ")
while len(first_name) > 10 or len(last_name) > 10:
    first_name = input("Nhap ten cua ban: ")
    last_name = input("Nhap ho cua ban: ")
print("Hello %s %s! You just delved into python."%(first_name, last_name))
