"""
0 so-bat-ky : them vao dau danh sach
1 so-bat-ky : them vao cuoi danh sach
2 : in va thoat
"""
class node ():
    def __init__(self, value): # dinh nghia kho co gia tri
        self.value = value
        self.next = None

class linked_list ():
    def __init__(self): # dinh nghia linked_lists
        self.head = None
        self.tail = None
    
    def __add_head__ (self, value):
        new_node = node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def __add_tail__(self, value):
        new_node = node(value)
        if self.head is None:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def __print__(self):
        i = self.head
        while i is not None:
            print(i.value, end = " ")
            i = i.next


if __name__ == "__main__":
    linkedLists = linked_list()
    print("Menu :\n0 - value : them dau danh sach\n1 - value : them cuoi danh sach\n2           : in danh sach va thoat")
    while (True):
        choice = int(input("Enter your choice : "))
        if choice == 0:
            value = int(input("Enter value: "))
            linkedLists.__add_head__(value)
        elif choice == 1: 
            value = int(input("Enter value: "))
            linkedLists.__add_tail__(value)
        else:
            linkedLists.__print__()
            break

