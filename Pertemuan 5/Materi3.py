#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

#============================================================
# Materi 3 Rekursif : Menjumlahkan Elemen List
#============================================================

def jumlah_list(data, index=0):
    # 1. Base Case (Kondisi Berhenti)
    # Kalau index sudah sama dengan panjang data, artinya semua angka sudah dilewati.
    # Kita balikin 0 karena angka 0 tidak akan merubah hasil penjumlahan.
    if index == len(data):
        return 0 
    
    # 2. Recursive Case (Pemanggilan Diri Sendiri)
    # Di sini program mengambil angka di index sekarang (misal: 2), 
    # terus ditambah hasil dari pemanggilan fungsi buat index berikutnya (index + 1).
    # Proses ini bakal terus berulang sampai index-nya mentok di ujung list.
    return data[index] + jumlah_list(data, index + 1)

# --- Bagian Eksekusi ---
print("===== Program Jumlah data =====")
# Memasukkan list [2, 4, 5], hasilnya nanti di terminal adalah 11
print("Hasil Penjumlahan List: ", jumlah_list([2, 4, 5]))