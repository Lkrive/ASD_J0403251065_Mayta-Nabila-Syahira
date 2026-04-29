#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 2 : Membuat Node Tree sampai Node G
#===============================================================

class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

# --- Level 0 ---
root = Node('A')

# --- Level 1 ---
root.left = Node('B')    
root.right = Node('C')   

# --- Level 2 ---
root.left.left = Node('D')   
root.left.right = Node('E')  

# --- Level 3 (Menambah F dan G) ---
# Kita hubungkan F dan G sebagai anak dari D
root.left.left.left = Node('F')  # F ada di bawah D sebelah kiri
root.left.left.right = Node('G') # G ada di bawah D sebelah kanan

# Menampilkan isi node untuk verifikasi
print("Data pada root          :", root.data)
print("Child Level 1           :", root.left.data, "dan", root.right.data)
print("Child dari B (Level 2)  :", root.left.left.data, "dan", root.left.right.data)
print("Child dari D (Level 3)  :", root.left.left.left.data, "dan", root.left.left.right.data)

#===============================================================
# Penjelasan:
#===============================================================
# 1. Untuk sampai ke node 'G', kita menambah satu tingkat lagi yaitu Level 3.
# 2. Perhatikan cara memanggilnya: 'root.left.left.left' untuk F. 
#    Artinya: Dari A -> ke B -> ke D -> baru ke F.
# 3. Ibarat silsilah keluarga, F dan G ini adalah 'cucu' dari B, 
#    atau 'cicit' dari si Root (A).
# 4. Semakin dalam pohonnya, semakin panjang deretan titik (.) yang 
#    digunakan untuk mengakses nodenya.