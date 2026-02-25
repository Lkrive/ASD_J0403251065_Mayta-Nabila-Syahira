#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# Rumus: a^n = a * a^(n-1)
# ==========================================================

def pangkat(a, n):
    # 1. Base Case (Kondisi Berhenti)
    # Jika pangkatnya adalah 0, maka hasilnya selalu 1 (semua angka pangkat 0 = 1).
    # Ini penting agar fungsi tidak berjalan terus-menerus tanpa henti.
    if n == 0:
        return 1
    
    # 2. Recursive Case (Pemanggilan Diri Sendiri)
    # Fungsi akan mengalikan 'a' dengan hasil pangkat (a, n-1).
    # n-1 bertujuan untuk mengurangi pangkat satu per satu sampai mencapai 0 (base case).
    return a * pangkat(a, n - 1)

# Mencoba menghitung 2 pangkat 4 (2^4)
# Alurnya: 2 * (2 * (2 * (2 * 1))) = 16
print("Hasil dari 2 pangkat 4 adalah:", pangkat(2, 4))