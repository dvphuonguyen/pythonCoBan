arrs = list(map(int,input().split(' ')))

maxa = arrs[0]
mina = arrs[0]

for element in arrs:
    if element > maxa:
        maxa= element
    if element < mina:
        mina = element

print(maxa, mina)
