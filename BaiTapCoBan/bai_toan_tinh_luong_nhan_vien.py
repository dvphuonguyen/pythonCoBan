#Bai toan tinh luong
''' Bài 2:Bạn là một kế toán của một công ty,
trách nhiệm của bạn là tính lươngcho các nhân viên trong công ty.
Lương của một nhân viên được tính theo công thức:
Lương = Lương cơ bản * Hệ số lương + Phụ cấp.
Hãy viết chương trình để có thể tính lương của một nhân viên nhanh chóng.'''

luong_co_ban = float(input("Nhap luong co ban: "))

he_so_luong = float(input("Nhap he so luong: "))

phu_cap = float(input("Nhap phu cap: "))

print("Luong cua mot nhan vien la: ",luong_co_ban * he_so_luong + phu_cap)
