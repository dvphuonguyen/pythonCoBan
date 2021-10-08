number = int(input())

stack_1 = list(map(int,input().split(' ')))

stack_2=[]

stack_3=[]

def insert_stack_new(values, stack_3):
    i = 0
    while i < len(stack_3):
        if values > stack_3[i]:
            stack_2.append(stack_3[i])
            stack_3.remove(stack_3[i])
        else:
            break
    stack_3.insert(0,values)
    
for index in range (number ):
    if index == (number - 1) :
        if stack_1[index] < stack_3[0]:
            stack_2.append(stack_1[index])
        elif stack_1[index] > stack_3[0]:
            insert_stack_new(stack_1[index], stack_3)
        stack_2 += stack_3
    elif stack_1[index] < stack_1[index + 1] :
        stack_2.append(stack_1[index])
    elif stack_1[index] > stack_1[index + 1]:
        if len(stack_3) == 0:
            stack_3.append(stack_1[index])
        elif stack_3[0] > stack_1[index]:
            stack_3.insert(0,stack_1[index])
        elif stack_3[0] < stack_1[index]:
            insert_stack_new(stack_1[index], stack_3)

#print(stack_2)
            
for key in range(number - 1):
    if stack_2[key] > stack_2[key + 1]:
        print("False")
        break
else:
    print("True")
