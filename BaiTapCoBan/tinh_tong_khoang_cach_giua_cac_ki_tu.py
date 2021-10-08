'''tinh khoang cach giua cac chu bat ki'''
string_1 = input("Nhap mot chuoi bat ki: ")

length = len(string_1)

distance = 0
for index in range (0, length):
    if index == 0:
        a = abs(ord(string_1[index]) - ord('a'))
        b = 26 - abs(ord(string_1[index ]) - ord('a'))
    else:
        a = abs(ord(string_1[index]) - ord(string_1[index - 1]))
        b = 26 - abs(ord(string_1[index ]) - ord(string_1[index -1]))
    distance += min (a, b)

print("Tong khoang cach la: ",distance )



import string
string_2 = input("Nhap mot chuoi bat ki: ")

flag = string.ascii_lowercase

distance_2 = 0
for i in range(len(string_2)):
    if i == 0:
        a = abs(flag.index(string_2[i]) - flag.index('a'))
        b = 26 - a
    else:
        a = abs(flag.index(string_2[i]) - flag.index(string_2[i - 1]))
        b = 26 - a
    distance_2 += min(a,b)
print("Tong khoang cach la: ",distance_2)
