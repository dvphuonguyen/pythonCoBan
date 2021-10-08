''' nhap so tien bat ki
va tinh cac to tien quy doi'''
money = float(input("Nhap mot khoang tien bat ki: "))

a,b,c,d,e,f,g,h,i = 0,0,0,0,0,0,0,0,0
while money > 0:
    if money >= 500000:
        money -= 500000
        a += 1
    elif money >=200000:
        money -= 200000
        b += 1
    elif money >= 100000:
        money -= 100000
        c += 1
    elif money >= 50000:
        money -= 50000
        d += 1
    elif money >= 20000:
        money -= 20000
        e += 1
    elif money >= 10000:
        money -= 10000
        f += 1
    elif money >= 5000:
        money -= 5000
        g += 1
    elif money >= 20000:
        money -= 20000
        h += 1
    elif money >= 1000:
        money -= 1000
        i += 1

print(f"{a} to 500k {b} to 200k {c} to 100k {d} to 50k {e} to 20k {f} to 10k {g} to 5k {h} to 2k {i} to 1k")
