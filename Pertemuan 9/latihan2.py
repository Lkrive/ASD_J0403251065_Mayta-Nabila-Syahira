#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 2 : Membuat Node Tree
#===============================================================

class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None # Memperbaiki typo 'rigt' menjadi 'right'

# Membuat root (Level 0)
root = Node('A')

# Membuat child Level 1
root.left = Node('B')    # Menghubungkan A ke B (kiri)
root.right = Node('C')   # Menghubungkan A ke C (kanan)

# Membuat child Level 2 (Dihubungkan ke node di Level 1)
root.left.left = Node('D')   # D menjadi anak kiri dari B
root.left.right = Node('E')  # E menjadi anak kanan dari B

# Menampilkan isi node untuk verifikasi
print("Data pada root          :", root.data)
print("Child kiri root (B)     :", root.left.data)
print("Child kanan root (C)    :", root.right.data)
print("Child kiri dari B (D)   :", root.left.left.data)
print("Child kanan dari B (E)  :", root.left.right.data)

#===============================================================
# Penjelasan:
#===============================================================
# 1. Struktur Tree dibangun dengan cara menghubungkan objek Node ke atribut 
#    'left' atau 'right' milik Node lainnya.
# 2. Node 'A' bertindak sebagai Root (induk tertinggi).
# 3. Node 'B' dan 'C' adalah anak langsung dari 'A' (Level 1).
# 4. Untuk membuat Level 2, kita harus mengakses anak dari Level 1. 
#    Contoh: 'root.left.left' artinya kita masuk ke node B, lalu mengisi 
#    tangan kirinya dengan node D.
# 5. Jika kita hanya menulis 'root.left = Node(D)', maka node B yang 
#    sudah ada sebelumnya akan tertimpa (terhapus) oleh node D.