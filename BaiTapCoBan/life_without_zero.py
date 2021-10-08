def life_without_zeros(lists):
    number = 0
    for index in range(len(lists)):
        if lists[index] != 0:
            number = lists[index] + number * 10
    return(number)


integer_a = input('Nhap so nguyen duong: ')

integer_b = input('Nhap so nguyen duong: ')

integer_c = str(int(integer_a) + int(integer_b))

integer_a = [int(i) for i in integer_a]

integer_b = [int(i) for i in integer_b]

integer_c = [int(i) for i in integer_c]

if life_without_zeros(integer_a) + life_without_zeros(integer_b) == life_without_zeros(integer_c):
    print('YES')
else:
    print('NO')

