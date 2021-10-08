'''tim so nguyen to max trong mang cac so nguyen'''
''' su dung ham'''
import math
arr = list(map(int, input().split()))

def SoNguyenTo(number):
    if number < 2:
        return 0
    else:
        for index in range(2, int(math.sqrt(number))):
            if number % index == 0:
                return 0
        return 1

flag = 0
max_snt = -1
for element in arr:
    if SoNguyenTo(element) == 1 and element > max_snt:
        max_snt = element

print(max_snt)
        
