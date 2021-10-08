number = int(input())

l = list(map(int,input().split(' ')))

left = 0
right = number - 1
number_1 = 0
number_2 = 0
for key in range (number):
    if key % 2 == 0:
        if(l[left] > l[right]):
             number_1 +=l[left]
             left +=1
        else:
            number_1 +=l[right]
            right -=1
    else:
        if(l[left] > l[right]):
             number_2 +=l[left]
             left +=1
        else:
            number_2 +=l[right]
            right -=1

#if number_1 > number_2:
print(number_1,number_2)
#else:
    #print(number_2,number_1)
