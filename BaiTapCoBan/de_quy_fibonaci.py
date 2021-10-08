''' fibonaci
0 1 1 2 3 5 ...'''
def fibonacci(number):
    if number < 2:
        return number
    else:
        return (fibonacci(number - 2) + fibonacci(number - 1))


number = int(input('Nhap so nguyen duong bat ki : ' ))

if number < 0:
    print("Khong co fibonacci")
else:
    print(fibonacci(number))
    
l = []               
def fibonacci_2(value):
    total = 0
    for index in range(0, value + 1):
        if index < 2:
            total = index
            l.append(total)
        else :
            total = l[index - 1] + l[ index -2]
            l.append(total)
    return l[value]

print(fibonacci_2(number))

''' su dung mang '''
def fibonacci_3(element):
    # se gay ra cap phat bo nho, ton nhieu bo nho
    # = > arrs = [none]* (element + 1)
    # arrs[0]= 0
    # arrs[1] = 1
    arrs = [0,1]
    if element < 2:
        return arrs[element]
    else:
        for index in range(2, element + 1):
            s = arrs[index - 1] + arrs[index -2]
            arrs.append(s)
            # arrs[index] = arrs[index - 1] + arrs[index -2]
        return arrs[element]
print(fibonacci_3(number)) 

''' su dung mang va kiem tra neu da co gia tri thi bo '''
 # = > arrs = [none]* (element + 1)
def fibonacci_4(arrs, number):
    if arrs[number] != None:
        return arrs[number]
    if number < 2:
        arrs[number] = number
    else:
        arrs[number] = fibonacci_4(arrs, number - 1) + fibonacci_4(arrs, number - 2)
    return arrs[number]

member = [None] *( number + 1)
print(fibonacci_4(member, number))


def fibonacci_5(arrs, number):
    if number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        arrs[number] = fibonacci_5(arrs, number - 1) + fibonacci_5(arrs, number - 2)
    return arrs[number]

member = [None] *( number + 1)
print(fibonacci_5(member, number))
