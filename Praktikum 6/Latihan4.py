#===============================================================
# Nama   : Mayta Nabila Syahira
# NIM    : J0403251065
# Kelas  : P/B2
#===============================================================

# ==========================================================
# Latihan 4 : Memahami Kode Program (Merge Sort)
# ==========================================================

def merge_sort(data):
    # Base Case: Mengembalikan data jika panjangnya 0 atau 1
    if len(data) <= 1:
        return data

    # Membagi data menjadi dua bagian (Divide)
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    # Memanggil kembali fungsi merge_sort (Recursive Call)
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Menggabungkan hasil sorting (Conquer)
    return merge_sort(left_sorted, right_sorted)

'''
Soal:
1. Apa yang dimaksud dengan base case?
2. Mengapa fungsi memanggil dirinya sendiri?
3. Apa tujuan fungsi merge()?

Jawaban :
1. Base case adalah kondisi berhenti agar fungsi rekursif tidak berjalan selamanya. 
   Pada kode ini, base case-nya adalah if len(data) <= 1, yang artinya jika 
   data sudah sisa 1 atau kosong, rekursi akan berhenti dan mengembalikan data.
2. Fungsi memanggil dirinya sendiri karena menggunakan teknik rekursi untuk 
   memecah masalah besar (list utuh) menjadi sub-masalah yang lebih kecil 
   (list terbagi dua) sampai ukuran terkecil agar lebih mudah dikelola.
3. Fungsi merge() bertujuan untuk menyatukan kembali (combine) dua list yang 
   telah terurut (left dan right) menjadi satu list baru yang tetap teratur 
   secara ascending.
'''