#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 6 : Membuat Struktur Organisasi dengan Tree
#===============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None # Perbaikan typo 'rigt'

# Fungsi untuk membaca struktur (Preorder: Atasan -> Bawahan Kiri -> Bawahan Kanan)
def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

# Membuat Root (Pucuk Pimpinan)
root = Node('Direktur')

# Level 1 (Manajer sebagai bawahan langsung Direktur)
root.left = Node('Manajer A')    
root.right = Node('Manajer B')

# Level 2 (Staff sebagai bawahan dari para Manajer)
root.left.left = Node('Staff 1')   # Bawahan Manajer A
root.left.right = Node('Staff 2')  # Bawahan Manajer A
root.right.right = Node('Staff 3') # Bawahan Manajer B

# Menampilkan hasil
print("Struktur Organisasi (Preorder):")
preorder(root)

#===============================================================
# Penjelasan:
#===============================================================
# 1. Di sini, Tree digunakan untuk memetakan rantai komando. 
#    'Direktur' menjadi Root atau pimpinan tertinggi.
# 2. 'Manajer A' dan 'Manajer B' adalah Child dari Direktur. Mereka berada 
#    di level yang sama (satu tingkat di bawah Direktur).
# 3. 'Staff 1' dan 'Staff 2' adalah Child dari 'Manajer A'. Ini berarti 
#    secara hirarki, mereka melapor ke Manajer A.
# 4. 'Staff 3' diletakkan di 'root.right.right', yang artinya dia adalah 
#    bawahan dari 'Manajer B' di sisi kanan.
# 5. Kenapa pakai Preorder? Karena Preorder mencetak dari ATASAN dulu 
#    baru ke BAWAHAN. Jadi urutannya enak dibaca: 
#    Direktur -> Manajer A -> Staff 1 -> Staff 2 -> Manajer B -> Staff 3.