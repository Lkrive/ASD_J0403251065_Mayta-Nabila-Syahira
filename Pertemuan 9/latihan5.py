#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 5 : Membuat Traversal Postorder
#===============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None # Memperbaiki typo 'rigt'

# Fungsi Postorder: Kiri ==> Kanan ==> Root
def postorder(node):
    if node is not None:
        # 1. Selesaikan semua urusan di kiri
        postorder(node.left)
        # 2. Selesaikan semua urusan di kanan
        postorder(node.right)
        # 3. Baru cetak data diri sendiri (Root)
        print(node.data, end=" ")

# Membangun struktur pohon
root = Node('A')

# Level 1
root.left = Node('B')
root.right = Node('C')

# Level 2 (Dihubungkan ke B agar struktur pohonnya benar)
root.left.left = Node('D')
root.left.right = Node('E')

# Menjalankan traversal
print("Hasil Traversal Postorder:")
postorder(root)

#===============================================================
# Penjelasan:
#===============================================================
# Bayangkan kamu adalah seorang kurir yang harus mengambil paket, 
# tapi aturannya: "Kamu baru boleh ambil paket di rumah induk kalau 
# semua paket di rumah anak (cabang) sudah diambil."
#
# 1. Kamu mulai dari A, tapi nggak boleh ambil paket di A. Kamu cek ke kiri (B).
# 2. Di B juga nggak boleh, cek lagi ke kiri (D).
# 3. Di D, karena nggak punya anak lagi, akhirnya kamu ambil paketnya. (Cetak: D)
# 4. Balik ke B? Belum boleh diambil! Kamu harus cek anak kanannya B dulu, yaitu E.
# 5. Di E, kamu ambil paketnya karena E nggak punya anak lagi. (Cetak: E)
# 6. Nah, karena anak kiri (D) dan anak kanan (E) sudah beres, baru deh kamu ambil di B. (Cetak: B)
# 7. Sekarang balik ke A? Belum boleh! Harus cek dulu cabang kanan A, yaitu C.
# 8. Di C, kamu ambil paketnya karena C nggak punya anak. (Cetak: C)
# 9. Terakhir, setelah semua cabang (B, D, E, C) selesai, barulah paket di A diambil. (Cetak: A)
#
# Hasil Akhirnya: D E B C A