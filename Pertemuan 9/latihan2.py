#===============================================================
# Nama   : Mayta Nabila Syahira
# NIM    : J0403251065
# Kelas  : P/B2
#===============================================================

#===============================================================
# Latihan 2 : Membuat Node Tree
#===============================================================

#class node digunakan dasar dari tree

class Node:
    def__init__(self, data):
    self.data = data #menimpan nilai node
    self.left = None #child kiri
    self.rigt = None #child kanan

#membuat sebuah node root
root = Node('A')

#membuat child Level 1
root.left = Node('B')
root.right = Node('C')

membuat child Level 2
root.left = Node('D')
root.right = Node('E')

#menampilkan isi node
print("Data pada root", root.data)
print("Child kiri root", root.left)
print("Child kanan root", root.right)
print("Child kiri dari B", root.left.left.data)
print("Child kanan dari B", root.right.right.data)


#Penjelasan : ...............................