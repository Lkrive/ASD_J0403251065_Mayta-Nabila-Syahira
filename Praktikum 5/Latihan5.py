#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

# ===========================================================
# Studi Kasus: Generator PIN (Rekursi dengan Loop)
# ===========================================================

def buat_pin(panjang, hasil=""):
    # 1. BASE CASE (Kondisi Berhenti)
    # Jika panjang string 'hasil' sudah sama dengan target 'panjang',
    # maka satu kombinasi PIN telah selesai dibentuk.
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return # Mengakhiri pemanggilan fungsi saat ini
    
    # 2. RECURSIVE CASE (Menggunakan Perulangan)
    # Untuk setiap angka dalam pilihan ["0", "1", "2"], fungsi akan
    # memanggil dirinya sendiri kembali.
    for angka in ["0", "1", "2"]:
        # Menambahkan angka terpilih ke dalam string 'hasil'
        # dan masuk ke kedalaman rekursi berikutnya.
        buat_pin(panjang, hasil + angka)

# Memanggil fungsi untuk membuat PIN dengan panjang 3
print("===== Daftar Generator PIN (Panjang 3) =====")
buat_pin(3)