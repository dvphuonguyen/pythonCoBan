''' tao class MONHOC '''
class MONHOC (object):
    def __init__(self, MAMH = '', TENMH = '', TCLT = 0, TCTH = 0):
        self.MAMH= MAMH
        self.TENMH = TENMH
        self.TCLT = TCLT
        self.TCTH = TCTH

    def input_information(self):
        self.MAMH = input('Enter MAMH: ')
        self.TENMH = input('Enter TENMH: ')
        self.TCLT = int(input('Enter TCLT: '))
        self.TCTH = int(input('Enter TCTH: '))
      
    def tc_lt_th(self):
        return self.TCLT + self.TCTH

    def output_information(self):
        print(self.MAMH," _ ", self.TENMH," _ ", self.TCLT, " _ ", self.TCTH)

    def __str__ (self):
        return f"({self.MAMH}, {self.TENMH}, {self.TCLT}, {self.TCTH})"

    def __repr__ (self):
        return str(self)

''' tao class HOCVIEN'''
class HOCVIEN (object):
    def __init__ (self, MAHV ='', HOTEN ='', GIOITINH = '',NGAYSINH  = ' ' , NOISINH = '', TCHIENTAI =  0, HOCKY = 0):
        self.MAHV = MAHV
        self.HOTEN = HOTEN
        self.GIOITINH = GIOITINH
        self.NGAYSINH = NGAYSINH
        self.NOISINH = NOISINH
        self.TCHIENTAI = TCHIENTAI
        self.HOCKY = HOCKY

    def input_inf(self):
        self.MAHV = input('Enter MAHV: ')
        self.HOTEN = input('Enter HOTEN: ')
        self.GIOITINH = input('Enter GIOITINH: ')
        self.NGAYSINH = input('Enter NGAYSINH: ')
        self.NOISINH = input('Enter NOISINH: ')
        self.TCHIENTAI = int(input('Enter TCHIENTAI: '))
        self.HOCKY = int(input('Enter HOCKY: '))

    def output_inf(self):
        print(self.MAHV," _ ", self.HOTEN," _ ", self.GIOITINH, " _ ", self.NGAYSINH, " _ ", self.NOISINH, " _ ",self.TCHIENTAI, " _ ", self.HOCKY)

    def __str__ (self):
        return f"({self.MAHV}, {self.HOTEN}, {self.GIOITINH}, {self.NGAYSINH}, {self.NOISINH}, {self.TCHIENTAI}, {self.HOCKY})"

    def __repr__ (self):
        return str(self)

'''tao class dkmh'''
arr= []
class DANGKYMONHOC (object):
    def __init__ (self,SOLUONGMONDANGKY = 1):
        self.hocvien = HOCVIEN()
        self.SOLUONGMONDANGKY = SOLUONGMONDANGKY
        b = MONHOC()
        self.monhocdangky = MONHOC()

    def input_info(self):
        self.hocvien.input_inf()
        self.SOLUONGMONDANGKY = int(input('Enter SOLUONGMONDANGKY: '))
        for index in range (0,self.SOLUONGMONDANGKY,1):
            self.monhocdangky.input_information()
            arr.append(self.monhocdangky)
       
    def tong_tc_sau_ki_dkhp (self):
        total = self.hocvien.TCHIENTAI 
        for index in range (self.SOLUONGMONDANGKY):
            total += arr[index].tc_lt_th()
        return total

    def output_info(self):
        self.hocvien.output_inf()
        print('So luong mon hoc da dang ki: ',self.SOLUONGMONDANGKY)
        for index in range (self.SOLUONGMONDANGKY):
            arr[index].output_information()
        print('Tong so tin chi da hoc : ', self.hocvien.TCHIENTAI)
        print('Tong so tin chi sau ki dang ki : ', self.tong_tc_sau_ki_dkhp())
        print('Tong so tin chi dang ky trong hoc ky nay : ',self.tong_tc_sau_ki_dkhp() -  self.hocvien.TCHIENTAI )
       
    def __str__ (object):
       return str(self.hocvien) + str(self.monhoc)

    def __repr__ (self):
       return str(self)





dkmh = []
'''1. nhap thong tin '''
numbers = int(input("Enter so luong hoc sinh: "))
for index in range (numbers):
    a = DANGKYMONHOC()
    a.input_info()
    dkmh.append(a)
'''2.xuat thong tin '''
for element in dkmh:
    element.output_info()
