#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 5 : Rotasi Kiri pada BST Tidak Seimbang
#===============================================================

class Node: 
    def __init__(self, data): 
        self.data = data      # Nilai utama si node
        self.left = None      # Tangan kiri
        self.right = None     # Tangan kanan

# Fungsi Preorder: Root -> Kiri -> Kanan
def preorder(root):     
    if root is not None: 
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right) 

# Fungsi Tampil Struktur: Biar kelihatan hierarkinya di terminal
def tampil_struktur(root, level=0, posisi="Root"):     
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L") 
        tampil_struktur(root.right, level + 1, "R") 

# --- INI LOGIKA PENTING: Fungsi Rotasi Kiri ---
def rotate_left(x): 
    # 1. x adalah si Bos lama yang mau kita geser ke bawah
    # 2. y adalah calon Bos baru (anak kanan si x)
    y = x.right       
    
    # 3. T2 adalah anak kiri si y (simpan dulu biar nggak ilang pas dipindah)
    T2 = y.left       

    # --- PROSES GESER ---
    # 4. y sekarang jadi atasan, dan x jadi anak kirinya y
    y.left = x        
    
    # 5. Bekas anak kiri y (T2) sekarang jadi anak kanan si x
    x.right = T2      

    # 6. Beritahu sistem kalau sekarang si y yang jadi Bos Utama (Root)
    return y 

# ----------------------------- 
# Program Utama 
# ----------------------------- 

# 1. Kita bikin pohon yang lurus miring ke kanan: 10 -> 20 -> 30
root = Node(10) 
root.right = Node(20) 
root.right.right = Node(30) 

print("Kondisi SEBELUM Rotasi Kiri:") 
preorder(root) 
print("\n\nStruktur Sebelum Rotasi:") 
tampil_struktur(root) 

print("\n" + "="*40)

# 2. Lakukan Rotasi Kiri pada si Root (angka 10)
root = rotate_left(root) 

print("Kondisi SESUDAH Rotasi Kiri:") 
preorder(root) 
print("\n\nStruktur Sesudah Rotasi:") 
tampil_struktur(root)

#===============================================================
# Penjelasan (Gaya Santai):
#===============================================================
# 1. Kenapa Harus Rotasi?
#    Karena awalnya pohon kamu "berat sebelah" ke kanan (10 -> 20 -> 30). 
#    Bayangkan ini kayak tiang yang mau roboh ke kanan, jadi harus kita 
#    tarik supaya tegak lagi.
#
# 2. Cara Kerjanya (Gaya Tarik):
#    Si angka 20 kita tarik ke atas untuk jadi Root. Karena 20 naik, 
#    otomatis angka 10 (Bos lama) kegeser ke bawah jadi anak kiri si 20. 
#    Sedangkan angka 30 tetep jadi anak kanan si 20.
#
# 3. Perubahan Hasilnya:
#    - Sebelum: Bentuknya lurus (10 -> 20 -> 30).
#    - Sesudah: Bentuknya jadi segitiga sempurna. 20 di puncak, 
#      10 di kiri, dan 30 di kanan.