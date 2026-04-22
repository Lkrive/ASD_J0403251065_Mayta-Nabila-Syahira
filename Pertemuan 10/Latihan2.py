#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 4 : Membuat BST yang Tidak Seimbang (Skewed Tree)
#===============================================================

class Node: 
    def __init__(self, data): 
        self.data = data      # Mengisi nilai angka ke dalam node
        self.left = None      # Tangan kiri (awal-awal masih kosong)
        self.right = None     # Tangan kanan (awal-awal masih kosong)

# Fungsi untuk memasukkan angka baru ke dalam pohon
def insert(root, data): 
    # Kalau tempatnya masih kosong (None), buat node baru di situ
    if root is None: 
        return Node(data) 

    # Kalau angka baru lebih kecil (<), suruh belok ke kiri
    if data < root.data: 
        root.left = insert(root.left, data) 

    # Kalau angka baru lebih besar (>), suruh belok ke kanan
    elif data > root.data: 
        root.right = insert(root.right, data) 

    # Kembalikan struktur pohon yang sudah diperbarui
    return root 

# Fungsi untuk membaca pohon (urutannya: Data -> Kiri -> Kanan)
def preorder(root):     
    if root is not None: 
        print(root.data, end=" ")   # Cetak data yang sedang dikunjungi
        preorder(root.left)         # Masuk ke cabang kiri
        preorder(root.right)        # Masuk ke cabang kanan

# Fungsi keren untuk gambar struktur pohon di terminal
def tampil_struktur(root, level=0, posisi="Root"):     
    if root is not None: 
        # Kasih spasi sesuai tingkatan (level) biar kelihatan menjorok
        print("   " * level + f"{posisi}: {root.data}") 
        # Panggil fungsi ini lagi untuk anak kiri (tambah levelnya)
        tampil_struktur(root.left, level + 1, "L") 
        # Panggil fungsi ini lagi untuk anak kanan (tambah levelnya)
        tampil_struktur(root.right, level + 1, "R") 

# ----------------------------- 
# Program Utama 
# ----------------------------- 

# 1. Mulai dengan pohon kosong
root = None 

# 2. Daftar angka yang mau dimasukkan (angkanya urut naik!)
data_list = [10, 20, 30]  

# 3. Masukkan angka satu per satu menggunakan looping
for data in data_list: 
    root = insert(root, data) 

# 4. Tampilkan hasil bacaan Preorder
print("Preorder BST:") 
preorder(root)  

# 5. Tampilkan bentuk pohonnya (pakai \n\n biar ada jarak/enter)
print("\n\nStruktur BST (Visualisasi Hirarki):") 
tampil_struktur(root)
#===============================================================
# Penjelasan:
#===============================================================
# 1. Kenapa disebut "Tidak Seimbang"? 
#    Coba lihat hasilnya nanti. Karena kita masukin angka 10, 20, 30 secara 
#    berurutan, maka setiap angka baru selalu LEBIH BESAR dari sebelumnya. 
#    Efeknya, semua angka bakal lari ke KANAN terus.
#
# 2. Skewed Tree (Pohon Miring):
#    Pohon kamu nggak punya cabang kiri sama sekali. Bentuknya jadi kayak 
#    garis lurus ke bawah (mirip Linked List).
#
# 3. Masalah Efisiensi:
#    Kalau pohonnya miring begini, keunggulan BST jadi hilang. Pas kita 
#    mau nyari angka 40, komputer tetep harus ngelewatin 10, 20, dan 30. 
#    Nggak bisa langsung "potong jalan" ke tengah.