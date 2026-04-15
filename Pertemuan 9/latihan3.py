#===============================================================
# Nama   : Mayta Nabila Syahira
# NIM    : J0403251065
# Kelas  : P/B2
#===============================================================

#===============================================================
# Latihan 1 : Membuat Travesal Preorder
#===============================================================

#class node digunakan dasar dari tree

class Node:
    def__init__(self, data):
    self.data = data #menimpan nilai node
    self.left = None #child kiri
    self.rigt = None #child kanan

#Fungsi preorder : Root ==> Left ==> Right
def preorder(node):
    if node is not None:
        print(node.data,  end=" ")
        preorder(node.left)
        preorder(node.right)

#membuat sebuah node root
root = Node('A')

#membuat child Level 1
root.left = Node('B')
root.right = Node('C')

membuat child Level 2
root.left = Node('D')
root.right = Node('E')

#menjalankan traversal preoorder
print('Hasil Traversal Preorder')
preorder(root)

Penjealasan=......


