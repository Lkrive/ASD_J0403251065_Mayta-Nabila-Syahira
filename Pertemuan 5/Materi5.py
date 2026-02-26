#===============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#===============================================================

#===============================================================
# Materi 5 Rekursif : Kombinasi Biner dengan Batas '1' (Pruning)
#===============================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # 1. PRUNING (Pemangkasan Cabang)
    # Jika jumlah angka '1' yang terkumpul sudah lebih besar dari batas,
    # langsung berhenti (return) dan jangan lanjut ke bawah. 
    # Ini bikin program lebih efisien karena nggak ngecek jalur yang udah pasti salah.
    if jumlah_1 > batas:
        return
    
    # 2. BASE CASE (Kondisi Berhenti)
    # Kalau panjang string 'hasil' sudah sesuai n, cetak hasilnya.
    if len(hasil) == n:
        print(hasil)
        return
    
    # 3. RECURSIVE CALL (Pilih '0')
    # Kalau nambah '0', variabel jumlah_1 tetap (tidak bertambah).
    biner_batas(n, batas, hasil + "0", jumlah_1)
    
    # 4. RECURSIVE CALL (Pilih '1')
    # Kalau nambah '1', variabel jumlah_1 ditambah 1.
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

# --- Bagian Eksekusi ---
print("===== Biner Panjang 4 dengan Maksimal Dua Angka '1' =====")
# Memanggil biner panjang 4, tapi angka '1'-nya maksimal cuma boleh 2 biji.
biner_batas(4, 2)