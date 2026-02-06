# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Mayta Nabila Syahira
# NIM : J0403251065
# Kelas : B2/P2
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
 with open(nama_file, "r", encoding="utf-8") as f:
  for baris in f:
    baris = baris.strip()
    if baris:
     kode, namabarang, stok = baris.split(",")
     stok_dict[kode] = {
      "Nama barang": namabarang, #key
      "Stok": int(stok)    #value
      }
 return stok_dict
#Memanggil fungsi untuk membaca data mahasiswa
buka_stok = baca_stok(nama_file)
#print("jumlah data terbaca", len(buka_data))


# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
 with open(nama_file, 'w') as file:
  for kode in stok_dict:
   namabarang = stok_dict[kode]['Nama barang']
   stok = stok_dict[kode]['Stok']
   file.write(f"{kode}, {namabarang}, {stok}\n")
#Memanggil fungsi untuk menyimpan data mahasiswa ke file
simpan_data_mahasiswa(nama_file, buka_data)
#print("data mahasiswa berhasil disimpan ke file."


 """
 Menyimpan seluruh data stok ke file teks.
 Format per baris: KodeBarang,NamaBarang,Stok
 """
 # TODO: Tulis ulang seluruh isi file berdasarkan stok_dict
 # Hint: with open(nama_file, "w", enco
 # -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
 """
 Menampilkan semua barang di stok_dict.
 """
 # TODO: Jika kosong, tampilkan pesan stok kosong
 # TODO: Tampilkan dengan format rapi: kode | nama | stok
 pass
# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
 """
 Mencari barang berdasarkan kode barang.
 """
 kode = input("Masukkan kode barang: ").strip()
 # TODO: Cek apakah kode ada di dictionary
 # Jika ada: tampilkan detail barang
 # Jika tidak ada: tampilkan 'Barang tidak ditemukan'
 pass
# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
 """
 Menambah barang baru ke stok_dict.
 """
 kode = input("Masukkan kode barang baru: ").strip()
 nama = input("Masukkan nama barang: ").strip()
 # TODO: Validasi kode tidak boleh duplikat
 # Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return
 # TODO: Input stok awal (integer)
 # Hint: stok_awal = int(input(...))
 # TODO: Simpan ke dictionary
 pass
# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
 """
 Mengubah stok barang (tambah atau kurangi).
 Stok tidak boleh menjadi negatif.
 """
 kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
# TODO: Cek apakah kode ada di dictionary
 # Jika tidak ada: tampilkan pesan dan return
 print("Pilih jenis update:")
 print("1. Tambah stok")
 print("2. Kurangi stok")
 pilihan = input("Masukkan pilihan (1/2): ").strip()
 # TODO: Input jumlah perubahan stok
 # Hint: jumlah = int(input("Masukkan jumlah: "))
 # TODO:
 # - Jika pilihan 1: stok = stok + jumlah
 # - Jika pilihan 2: stok = stok - jumlah
 # - Jika hasil < 0: batalkan dan tampilkan error
 pass
# -------------------------------
# Program Utama
# -------------------------------
def main():
 # Membaca data dari file saat program mulai
 stok_barang = baca_stok(NAMA_FILE)
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
 simpan_stok(NAMA_FILE, stok_barang)
 print("Data berhasil disimpan.")
 elif pilihan == "0":
 print("Program selesai.")
 break
else:
 print("Pilihan tidak valid. Silakan coba lagi.")
# Menjalankan program utama
if __name__ == "__main__":
 main()
