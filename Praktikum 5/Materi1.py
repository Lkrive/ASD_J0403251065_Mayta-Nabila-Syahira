#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

#============================================================
# Materi 1 Rekursif : Faktorial
#  3! = 3 x 2 x 1 
# Base Case => 0 (Berhenti, hingga fungsi tidak jalan terus menerus)
# Recucrsive Case (Pemanggilan fungsinya sndiri dgn ukuran yang 
# dikurangi)
#============================================================

def faktorial(n):
    # 1. Base Case (Titik Berhenti)
    # Ini rem-nya, kalau n sudah 0, kita balikin angka 1.
    # Kenapa 1? Karena kalau dikali 0 nanti hasilnya jadi 0 semua. [cite: 572]
    if n == 0:
        return 1
    
    # 2. Recursive Case (Panggil Diri Sendiri)
    # Di sini angkanya dikali terus sama fungsi itu sendiri tapi n-nya dikurangin 1.
    # Jadi kayak tangga, turun terus (3 * 2 * 1) sampai nabrak Base Case di angka 0.
    return n * faktorial(n - 1) 

# --- Bagian Eksekusi ---
print("========= Program Faktorial ==========")
# Di sini kita coba hitung 3!, nanti di terminal munculnya 6.
print("Hasil Faktorial : ", faktorial(3))