#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

#============================================================
# Materi 2 Rekursif : Call Stack
# Stracing bilangan (masuk-keluar)
#input 3
# Masuk 1 - 2 - 3
# Keluar
#3-2-1 | 1-2-3
#============================================================

def hitung(n):
    # 1. Base Case (Titik Berhenti)
    # Kalau n sudah 0, program berhenti biar nggak jalan terus (infinite loop).
    # Pas di sini, program bakal cetak "selesai" dan mulai balik ke atas.
    if n == 0:
        print("selesai")
        return 
    
    # 2. Fase "Masuk" (Wind-up)
    # Program cetak angka n dulu sebelum dia masuk ke pemanggilan rekursif berikutnya.
    # Urutannya bakal dari gede ke kecil (5, 4, 3, 2, 1).
    print("Masuk: ", n)
    
    # 3. Recursive Case (Pemanggilan Diri Sendiri)
    # Di sini fungsinya panggil diri sendiri tapi angkanya dikurang 1 (n-1).
    # Perlu diingat, perintah cetak "Keluar" di bawahnya bakal "DIPENDING" dulu di memori (Stack).
    hitung(n-1) 
    
    # 4. Fase "Keluar" (Unwinding / Backtracking)
    # Ini dijalankan pas program udah selesai dari base case dan mulai bongkar tumpukan memori.
    # Makanya urutan angkanya bakal kebalik (1, 2, 3, 4, 5).
    print("Keluar", n)

# --- Bagian Eksekusi ---
print("================= Program Tracing ==============")
# Kita mulai panggil dari angka 5
hitung(5)