#===============================================================
# Nama   : Mayta Nabila Syahira
# NIM    : J0403251065
# Kelas  : P/B2
#===============================================================

#===============================================================
# Latihan 1 : Membuat Travesal Ineorder
#===============================================================

#class node digunakan dasar dari tree

class node:
    def__init__(self, data):
    self.data = data #menimpan nilai node
    self.left = None #child kiri
    self.rigt = None #child kanan

#membuat fungsi inorder: left ==> root ==> right
def inorder(nade):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)
        



#membuat sebuah node root
root = Node('A')

#membuat child Level 1
root.left = Node('B')
root.right = Node('C')

membuat child Level 2
root.left = Node('D')
root.right = Node('E')

#menjalankan traversal 
print("Hasil Traversal Inorder")
inorder(root)

Penjelasan:...