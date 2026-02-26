#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

#============================================================
# Materi 4 Rekursif : Konsep Dasar Backtracing
# Kombinasi Biner (n) 
#============================================================

def biner(n, hasil=""):
    # 1. Base Case (Kondisi Berhenti)
    # Kalau panjang string 'hasil' sudah sama dengan n,
    # berarti satu urutan biner sudah jadi dan siap dicetak ke terminal.
    if len(hasil) == n:
        print(hasil)
        return # Kembali ke tumpukan sebelumnya (backtracking)
    
    # 2. Choose + Explore (Cabang Kiri: Tambah '0')
    # Program bakal nyoba nambahin angka '0' dulu sampai mentok ke base case.
    biner(n, hasil + "0")
    
    # 3. Choose + Explore (Cabang Kanan: Tambah '1')
    # Setelah urutan yang diawali '0' selesai, program balik lagi
    # buat nyoba nambahin angka '1'.
    biner(n, hasil + "1")

# --- Bagian Eksekusi ---
print("===== Daftar Kombinasi Biner (n=3) =====")
# Memanggil fungsi untuk panjang 3, totalnya bakal ada 8 kombinasi (2^3)
biner(3)