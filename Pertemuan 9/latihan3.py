#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 3 : Membuat Traversal Preorder
#===============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None # Memperbaiki typo 'rigt'

# Fungsi preorder menggunakan prinsip: Root -> Left -> Right
def preorder(node):
    if node is not None:
        # 1. Kunjungi Root (Cetak data)
        print(node.data, end=" ")
        # 2. Rekursif ke sub-pohon kiri
        preorder(node.left)
        # 3. Rekursif ke sub-pohon kanan
        preorder(node.right)

# Membangun struktur pohon
root = Node('A')

# Level 1
root.left = Node('B')
root.right = Node('C')

# Level 2 (Dihubungkan ke B agar menjadi satu kesatuan pohon)
root.left.left = Node('D')
root.left.right = Node('E')

# Menjalankan traversal preorder
print('Hasil Traversal Preorder:')
preorder(root)

#===============================================================
# Penjelasan:
#===============================================================
# 1. Traversal Preorder adalah teknik kunjungan pohon dengan urutan 
#    Data (Root) -> Kiri -> Kanan.
# 2. Fungsi ini bekerja secara 'rekursif', artinya fungsi memanggil 
#    dirinya sendiri untuk menjelajahi setiap cabang hingga ujung terdalam.
# 3. Alur pada kode di atas:
#    - Cetak 'A' (Root).
#    - Pergi ke kiri ke node 'B', cetak 'B'.
#    - Pergi ke kiri lagi ke node 'D', cetak 'D'.
#    - Karena 'D' tidak punya anak, fungsi kembali ke 'B' dan mengecek 
#      anak kanan yaitu 'E', lalu cetak 'E'.
#    - Terakhir, kembali ke paling atas untuk mengecek anak kanan 'A' 
#      yaitu 'C', lalu cetak 'C'.
# 4. Maka hasil akhirnya adalah: A B D E C.