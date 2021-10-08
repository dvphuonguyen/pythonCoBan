# Enter your code here. Read input from STDIN. Print output to STDOUT
# Nhap so luong nguoi co sdt
numbers = int(input())
# Khoi t bien chua gia tri ten va sdt
dicts = {}
# nhap ten va sdt cua khach do
#index = 0
while (True):
    try:
        # Nhap ten va sdt duoi dang list
        value =input().split(' ')
        if (len(value) > 1):
        # neu chieu dai cua value > 1 tuc la co 2 gia tri vao 
        # nam va sdt
        # them vao dicts
            dicts[value[0]]= value[1]
        elif value[0] in dicts:
        # Nguoc lai thi xet xem value[0] co sdt nam trong dict k
        # neu co, xuat sdt
        # ngc lai, xuat 'Not found'
            print("{0}={1}".format(value[0], dicts[value[0]]))
        else:
            print('Not found')
        #index += 1
    except:
        break