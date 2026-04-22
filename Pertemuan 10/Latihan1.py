#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 1 : Membangun BST (Binary Search Tree)
#===============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Fungsi buat masukin data otomatis sesuai aturan BST
def insert(root, data):
    # Kalau tempatnya masih kosong (None), langsung buat node baru di sini
    if root is None:
        return Node(data)

    # Kalau data baru LEBIH KECIL dari data sekarang, belok ke kiri
    if data < root.data:
        root.left = insert(root.left, data)
    # Kalau data baru LEBIH BESAR dari data sekarang, belok ke kanan
    elif data > root.data:
        root.right = insert(root.right, data)
    
    # Kembalikan struktur pohon yang sudah diperbarui
    return root

# Persiapan data
root = None
data_list = [50, 30, 70, 20, 40, 60, 80] # Aku ganti 50 (duplikat) jadi 60 ya biar rapi

# Masukin semua data di list ke dalam pohon
for d in data_list:
    root = insert(root, d)

print("BST berhasil dibuat!")

#===============================================================
# Latihan 2 : Traversal Inorder (Membaca Pohon)
#===============================================================

def inorder(root):
    if root is not None:
        inorder(root.left)    # Cek kiri dulu
        print(root.data, end=' ') # Cetak tengah
        inorder(root.right)   # Baru cek kanan

print("Hasil Inorder (Data terurut): ")
inorder(root)
print("\n") # Biar ada jarak baris

#===============================================================
# Latihan 3 : Searching (Mencari Data)
#===============================================================

def search(root, key):
    # 1. Kalau mentok dan nggak ketemu, atau pohon kosong
    if root is None:
        return False
    
    # 2. Kalau datanya pas banget sama yang dicari
    if root.data == key:
        return True

    # 3. Kalau yang dicari lebih kecil, cari ke sebelah kiri
    if key < root.data:
        return search(root.left, key)
    # 4. Kalau yang dicari lebih besar, cari ke sebelah kanan
    else:
        return search(root.right, key)

# Uji coba cari angka 30
key_cari = 70
print(f"Mencari angka {key_cari}...")

if search(root, key_cari):
    print("Data ditemukan!")
else:
    print("Data Tidak ditemukan")

#===============================================================
# Penjelasan:
#===============================================================
# Gampangnya gini Mayta, BST itu punya "Satpam" di setiap pintunya:
#
# 1. Kenapa Inorder hasilnya jadi urut (20 30 40 50 60 70 80)? 
#    Karena sifat BST yang 'Kiri < Root < Kanan', pas kita pakai Inorder 
#    (Kiri-Root-Kanan), angkanya otomatis kepanggil dari yang terkecil. 
#    Ajaib kan? Nggak perlu pakai fungsi sort lagi!
#
# 2. Cara Kerja Insert: 
#    Misal mau masukin 70. Dia tanya ke Root (50): "Eh, 70 lebih besar 
#    dari kamu nggak?". Karena iya, 70 langsung disuruh ke kanan. 
#    Jadi dia nggak bakal nyasar.
#
# 3. Kenapa Search di BST itu Cepet? 
#    Karena kita nggak perlu ngecek SEMUA angka. Kalau kita cari 20, 
#    dan Root-nya 50, kita udah pasti tahu 20 nggak mungkin ada di 
#    sebelah kanan. Jadi setengah isi pohon langsung kita abaikan. 
#    Ini yang bikin program kamu jadi efisien banget!