#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

# ==========================================================
# Latihan 4: Kombinasi Huruf (A dan B)
# ==========================================================

def kombinasi(n, hasil=""):
    # 1. BASE CASE (Kondisi Berhenti)
    # Jika panjang string 'hasil' sudah sama dengan n,
    # artinya satu kombinasi sudah lengkap dan siap dicetak.
    if len(hasil) == n:
        print(hasil)
        return # Kembali ke tumpukan sebelumnya untuk mencari cabang lain
    
    # 2. RECURSIVE CALL (Percabangan)
    # Rekursi pertama: Menambahkan huruf "A" ke kombinasi saat ini
    kombinasi(n, hasil + "A")
    
    # Rekursi kedua: Menambahkan huruf "B" ke kombinasi saat ini
    # Ini dijalankan setelah cabang "A" selesai diproses sampai tuntas.
    kombinasi(n, hasil + "B")

# Memanggil fungsi untuk membuat kombinasi dengan panjang 2
print("===== Daftar Kombinasi (n=2) =====")
kombinasi(2)