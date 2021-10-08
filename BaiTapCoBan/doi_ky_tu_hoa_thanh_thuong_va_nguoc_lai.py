''' doi chu hoa thanh chu thuong va nguoc lai'''
string_1 = input("Nhap mot chuoi bat ki: ")

new = ''
for index in range (len(string_1)):
    if string_1[index] >='a' and string_1[index] <='z':
        #string_1[index].isupper()
         new += string_1[index].upper()
    elif string_1[index] >='A' and string_1[index] <='Z':
        #string_1[index].islower()
          new += string_1[index].lower()
    else:
        new += string_1[index]
print("Chuoi moi: ",new)



