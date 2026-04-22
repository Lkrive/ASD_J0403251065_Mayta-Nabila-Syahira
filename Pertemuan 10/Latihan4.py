#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 6 : Rotasi Kanan pada BST Tidak Seimbang
#===============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Fungsi Preorder untuk cek urutan (Root -> Kiri -> Kanan)
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi Visualisasi Hirarki
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("   " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# --- INI INTI MATERINYA: Fungsi Rotasi Kanan ---
def rotate_right(y):
    # 1. y adalah Bos lama (si 30) yang miring ke kiri
    # 2. x adalah calon Bos baru (anak kiri si y, yaitu si 20)
    x = y.left
    
    # 3. T2 adalah anak kanan si x (simpan dulu supaya tidak terputus)
    T2 = x.right

    # --- PROSES ROTASI ---
    # 4. x naik pangkat jadi Bos, dan y turun jadi anak kanannya x
    x.right = y
    
    # 5. Bekas anak kanan x (T2) sekarang jadi anak kiri si y
    y.left = T2

    # 6. Beritahu sistem kalau sekarang x (si 20) yang jadi pusat/Root
    return x

# -----------------------------
# Program Utama
# -----------------------------

# 1. Membuat pohon yang miring ke kiri (30 -> 20 -> 10)
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Kondisi SEBELUM Rotasi Kanan:")
preorder(root)
print("\n\nStruktur Sebelum Rotasi:")
tampil_struktur(root)

print("\n" + "="*40)

# 2. Lakukan Rotasi Kanan pada root (angka 30)
root = rotate_right(root)

print("Kondisi SESUDAH Rotasi Kanan:")
preorder(root)
print("\n\nStruktur Sesudah Rotasi:")
tampil_struktur(root)

#===============================================================
# Penjelasan:
#===============================================================
# 1. Kenapa Harus Rotasi Kanan?
#    Karena data yang dimasukkan (30, 20, 10) bikin pohon kamu "Keberatan 
#    Kiri". Angka 20 lebih kecil dari 30 (masuk kiri), dan 10 lebih kecil 
#    dari 20 (masuk kiri lagi). Bentuknya jadi miring kayak perosotan.
#
# 2. Cara Kerjanya (Gaya Dorong):
#    Kita ambil node tengah (20) lalu kita dorong/putar ke arah kanan. 
#    Hasilnya, si 30 yang tadinya Bos besar sekarang "turun jabatan" 
#    menjadi anak kanan dari si 20.
#
# 3. Hasil Akhir yang Aesthetic:
#    Setelah diputar, si 20 berdiri tegak di tengah (Root). Dia punya 
#    tangan kiri (10) dan tangan kanan (30). Pohon jadi seimbang sempurna!
#
# 4. Kesimpulannya:
#    Rotasi Kanan adalah solusi buat pohon yang miring ke kiri. Dengan 
#    begini, struktur data kamu nggak cuma rapi dilihat, tapi juga 
#    bikin proses pencarian angka di komputer jadi jauh lebih efisien.