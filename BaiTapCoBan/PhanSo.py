class PhanSo:
    def __init__(self):
        self.tu_so = 0
        self.mau_so = 1

    def __change__(self, int):
        self.tu_so = int
        self.mau_so = 1

    def __input__(self):
        self.tu_so = float(input("Enter tu so: "))
        self.mau_so = float(input("Enter mau so: "))

    def __output__(self):
        return ("%d / %d") %(self.tu_so, self.mau_so)

    def __sum__(self, other):
        tong = PhanSo()
        tong.tu_so = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        tong.mau_so = self.mau_so * other.mau_so
        return tong

    def __sub__(self, other):
        hieu = PhanSo()
        hieu.tu_so = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        hieu.mau_so = self.mau_so * other.mau_so
        return hieu

    def __mul__(self, other):
        tich = PhanSo()
        tich.tu_so = self.tu_so * other.tu_so
        tich.mau_so = self.mau_so * other.mau_so
        return tich

    def __div__(self, other):
        thuong = PhanSo()
        thuong.tu_so = self.tu_so * other.mau_so
        thuong.mau_so = self.mau_so * other.tu_so
        return thuong

    def __ucln__(self):
        if self.tu_so == 0 or self.mau_so == 0:
            return 0
            
        a = self.tu_so
        b = self.mau_so

        while ( a != b):
            if a > b:
                a = a - b
            else :
                b = b - a
        return a

    def __rutgon__(self):
        a = self.__ucln__()
        self.tu_so = self.tu_so / a
        self.mau_so = self.mau_so / a
        if self.mau_so == 0:
            return False
        elif self.tu_so == 0:
            return 0
        elif self.mau_so == 1:
            return self.tu_so
        else:
            return  ("%d / %d") %(self.tu_so, self.mau_so)

if __name__ == "__main__":
    print("BEGIN THE PROGRAM: ")
    # Khai bao va nhap phan so thu nhat
    print("---Khai bao va nhap phan so thu nhat: ---")
    phan_so_thu_nhat = PhanSo()
    phan_so_thu_nhat.__input__()
    # Khai bao va nhap phan so thu hai
    print("---Khai bao va nhap phan so thu hai: ---")
    phan_so_thu_hai = PhanSo()
    phan_so_thu_hai.__input__()

    # Bat dau tinh toan
    print("---Thuc hien cac phep tinh: ---")
    # Tinh tong hai phan so
    Tong = phan_so_thu_nhat.__sum__(phan_so_thu_hai)
    print ("Tong hai phan so la: ", Tong.__output__())
    print ("Tong hai phan so sau khi rut gon la: ", Tong.__rutgon__())
    # Tinh hieu hai phan so
    Hieu = phan_so_thu_nhat.__sub__(phan_so_thu_hai)
    print ("Tong hai phan so la: ", Hieu.__output__())
    print ("Tong hai phan so sau khi rut gon la: ", Hieu.__rutgon__())
    # Tinh tich hai phan so
    Tich = phan_so_thu_nhat.__mul__(phan_so_thu_hai)
    print ("Tong hai phan so la: ", Tich.__output__())
    print ("Tong hai phan so sau khi rut gon la: ", Tich.__rutgon__())
    # Tinh thuong hai phan so
    Thuong = phan_so_thu_nhat.__div__(phan_so_thu_hai)
    print ("Tong hai phan so la: ", Thuong.__output__())
    print ("Tong hai phan so sau khi rut gon la: ", Thuong.__rutgon__())
    # Ket thuc chuong trinh
    print("THE END")
    

    

    

