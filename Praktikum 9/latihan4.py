#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 4 : Membuat Traversal Inorder
#===============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None # Perbaikan typo 'rigt'

# Fungsi Inorder: Kiri ==> Root ==> Kanan
def inorder(node):
    if node is not None:
        # 1. Pergi sejauh mungkin ke kiri
        inorder(node.left)
        # 2. Cetak data (Root/Tengah)
        print(node.data, end=" ")
        # 3. Baru pergi ke kanan
        inorder(node.right)

# Membangun struktur pohon yang benar
root = Node('A')

# Level 1
root.left = Node('B')
root.right = Node('C')

# Level 2 (Dihubungkan ke B)
root.left.left = Node('D')
root.left.right = Node('E')

# Menjalankan traversal
print("Hasil Traversal Inorder:")
inorder(root)

#===============================================================
# Penjelasan:
#===============================================================
# Bayangkan kamu lagi jalan-jalan di pohon, tapi aturannya: 
# "Jangan sentuh induknya kalau kirinya belum habis dikunjungi."
#
# 1. Dari A, kita nggak boleh cetak A dulu, kita harus cek kirinya (B).
# 2. Di B, kita juga nggak boleh cetak B, cek lagi kirinya (D).
# 3. Di D, karena nggak punya anak kiri lagi, baru deh kita cetak 'D'.
# 4. Setelah D selesai, kita naik balik ke induknya yaitu 'B', lalu cetak 'B'.
# 5. Habis dari B, kita pindah ke kanannya B yaitu 'E', lalu cetak 'E'.
# 6. Karena semua urusan di cabang kiri (A) sudah beres (D-B-E), baru kita cetak 'A'.
# 7. Terakhir, kita pindah ke cabang kanan 'A' yaitu 'C', lalu cetak 'C'.
#
# Jadi, hasil akhirnya adalah: D B E A C.
# Urutan ini kayak kita ngebaca dari arah kiri ke kanan secara mendatar.