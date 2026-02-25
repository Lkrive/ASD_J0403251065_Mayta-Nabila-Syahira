#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

# ==========================================================
# Latihan 2: Tracing Rekursi Countdown
# ==========================================================

def countdown(n):
    # 1. Base Case: Kondisi di mana rekursi harus berhenti.
    # Jika n sudah mencapai 0, cetak "Selesai" dan hentikan fungsi (return).
    if n == 0:
        print("Selesai")
        return
    
    # 2. Fase Menuju Rekursi (Wind-up):
    # Mencetak angka n saat ini sebelum memanggil dirinya sendiri.
    print("Masuk:", n)
    
    # 3. Recursive Call:
    # Memanggil kembali fungsi countdown dengan nilai n yang dikurangi 1.
    # Program akan "menumpuk" panggilan ini di memori (Stack).
    countdown(n - 1)
    
    # 4. Fase Setelah Rekursi (Unwinding):
    # Baris ini HANYA akan dieksekusi SETELAH fungsi countdown(n-1) selesai.
    # Inilah alasan mengapa angka muncul dengan urutan terbalik saat "Keluar".
    print("Keluar:", n)

# Menjalankan program dengan angka 3
print("===== Memulai Tracing Rekursi =====")
countdown(3)