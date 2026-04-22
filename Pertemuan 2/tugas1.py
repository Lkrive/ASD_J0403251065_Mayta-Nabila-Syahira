# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Mayta Nabila Syahira
# NIM : J0403251065
# Kelas : P/B2
# ==========================================================
# -------------------------------
# Konstanta nama file
# -------------------------------
nama_file = "stok_barang.txt"
# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    stok_dict = {}
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                baris = baris.strip()
                if baris:
                    kode, nama_barang, stok = baris.split(",")
                    stok_dict[kode] = {
                        "Nama": nama_barang,
                        "Stok": int(stok)
                    }
    except FileNotFoundError:
        print("File stok belum ada. Membuat data stok kosong...")
    return stok_dict
#Memanggil fungsi untuk membaca stok barang
#buka_stok = baca_stok(nama_file)
#print("jumlah data terbaca", len(buka_stok))


# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
#Memanggil fungsi untuk menyimpan data mahasiswa ke file
def simpan_stok(nama_file, stok_dict):
  with open(nama_file, 'w') as file:
   for kode in stok_dict:
    nama_barang = stok_dict[kode]['Nama']
    stok = stok_dict[kode]['Stok']
    file.write(f"{kode}, {nama_barang}, {stok}\n")
print("Data berhasil disimpan ke file.")

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
 if len(stok_dict) == 0:
  print("Maaf, stok kosong")
  return
 
 #membuat headertable
 print("========Daftar Stok barang========")
 print(f"{'Kode':<10} | {'Nama':<12} | {'Stok':>5}")
 print("-" * 32)

 '''
untuk tampilan yang rapi, atur f-string formating
{'Kode ':<10} artinya lebar kolom NIM 10 karakter, rata kiri
{'Nama barang':<12} artinya lebar kolom Nama 12 karakter, rata kiri    {'Stok':>5} artinya lebar kolom Nilai 5 karakter, rata kanan
cetak - sebanyak 32 kali
 '''

 for kode in sorted(stok_dict.keys()):
  nama_barang = stok_dict[kode]['Nama']
  stok = stok_dict[kode]['Stok']
  print(f"{kode:<10} | {nama_barang:<12} |{stok:>5}")

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------

def cari_barang(stok_dict):
 kode_cari= input("masukan Kode barang yang dicari: ")
 if kode_cari in stok_dict:
   nama_barang = stok_dict[kode_cari]['Nama']
   stok = stok_dict[kode_cari]['Stok']

   print('Barang ditemukan: ')
   print(f'Kode:{kode_cari}')
   print(f'Nama:{nama_barang}')
   print(f'Stok:{stok}')
 else:
  print('Barang tidak ditemukan.')

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    kode = input("Masukkan kode barang baru: ").strip()

    # Validasi kode duplikat 
    if kode in stok_dict:
        print("Kode sudah digunakan")
        return

    nama = input("Masukkan nama barang: ").strip()

    try:
        stok_awal = int(input("Masukkan stok awal: "))
    except ValueError:
        print("Stok harus berupa angka")
        return

    stok_dict[kode] = {
        "Nama": nama,
        "Stok": stok_awal
    }

    print("Barang berhasil ditambahkan")


# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    if kode not in stok_dict:
        print("Kode tidak ditemukan. Update dibatalkan")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()

    try:
        jumlah = int(input("Masukkan jumlah (0-100): "))
    except ValueError:
        print("Jumlah harus berupa angka")
        return

    stok_lama = stok_dict[kode]["Stok"]

    if pilihan == "1":
        stok_baru = stok_lama + jumlah
    elif pilihan == "2":
        stok_baru = stok_lama - jumlah
    else:
        print("Pilihan tidak valid. Update dibatalkan")
        return

    if stok_baru < 0:
        print("Stok tidak boleh negatif. Update dibatalkan")
        return

    stok_dict[kode]["Stok"] = stok_baru
    print(f"Update berhasil. Stok {kode} berubah dari {stok_lama} menjadi {stok_baru}")


# -------------------------------
# Program Utama
# -------------------------------
def main():
    stok_barang = baca_stok(nama_file)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")
if __name__ == "__main__":
    main()
