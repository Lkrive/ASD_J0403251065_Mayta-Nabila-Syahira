#========================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#========================================================


#========================================================
# Pratikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 1: Membuat fungsi dan load data
#========================================================

nama_file ="data_mahasiswa.txt"
#Fungsi untuk membaca data mahasiswa dari file dan menyimpannya dalam dictionary
def baca_data_mahasiswa(nama_file):
    data_dict = {} #Inisialisasi data dictionary kosong
    # MEMPERBAIKI: Menggunakan mode 'r' (read) bukan 'w' (write) agar bisa dibaca
    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                baris = baris.strip() #Menghilangkan karakter newline dan spasi di awal/akhir (\n)
                if baris: # Tambahan: pastikan baris tidak kosong
                    nim, nama, nilai = baris.split(',') #parsing data berdasarkan karakter ,    
                #simpan data ke dictionary dengan NIM sebagai key
                    data_dict[nim] = {
                    'nama': nama, 
                    'nilai': int(nilai)
                    }
    except FileNotFoundError:
        # Jika file belum ada, buat file kosong biar tidak crash
        open(nama_file, 'a').close()
    return data_dict

#Memanggil fungsi untuk membaca data mahasiswa
buka_data = baca_data_mahasiswa(nama_file)
#print("jumlah data terbaca", len(buka_data))

#========================================================
# Pratikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 2: Membuat fungsi menampilkan data
#========================================================

def tampilkan_data(data_dict):
    if len(data_dict) == 0:
        print("data mahasiswa kosong")
        return
#membuat header table
    print("=====daftar mahasiswa=====")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>5}")
    print("-" * 32)
    
    '''
    untuk tampilan yang rapi, atur f-string formating
    {'NIM':<10} artinya lebar kolom NIM 10 karakter, rata kiri
    {'Nama':<12} artinya lebar kolom Nama 12 karakter, rata kiri
    {'Nilai':>5} artinya lebar kolom Nilai 5 karakter, rata kanan
    '''
    
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]['nama']
        nilai = data_dict[nim]['nilai']
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")
#Memanggil fungsi untuk menampilkan data mahasiswa
#tampilkan_data(buka_data)

#========================================================
# Pratikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 3: Membuat fungsi mencari data (opsional)
#========================================================

def cari_data(data_dict):
    #mencari data mahasiswa berdasarkan NIM
    nim_cari = input("masukkan NIM yang dicari: ")
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]['nama']
        nilai = data_dict[nim_cari]['nilai']

        print("data mahasiswa ditemukan:")
        print(f"NIM: {nim_cari}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    else:
        print("data mahasiswa tidak ditemukan.")

#========================================================
# Pratikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 4: Membuat fungsi Update nilai mahasiswa
#========================================================
def update_nilai(data_dict):
    #mengupdate nilai mahasiswa berdasarkan NIM
    nim = input("masukkan NIM yang akan diupdate nilainya: ").strip()
    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    try:
        nilai_baru = int(input("masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("nilai harus berupa angka. Update dibatalkan")
        return
    if nilai_baru < 0 or nilai_baru > 100:
        print("nilai harus antara 0-100. Update dibatalkan")
        return
    nilai_lama = data_dict[nim]['nilai']
    
    data_dict[nim]['nilai'] = nilai_baru
    print(f"update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")
#Memanggil fungsi untuk mengupdate nilai mahasiswa
#update_nilai(buka_data)

#===========================================================
# Praktikum 2 : Konsep ADT dan file handling (Studi Kasus)
# Latihan 5 : Membuat fungsi menyimpan perubahan data ke file
# ===========================================================

def simpan_data_mahasiswa(nama_file, data_dict):
    with open(nama_file, 'w') as file:
        for nim in data_dict:
            nama = data_dict[nim]['nama']
            nilai = data_dict[nim]['nilai']
            file.write(f"{nim},{nama},{nilai}\n")
#Memanggil fungsi untuk menyimpan data mahasiswa ke file
simpan_data_mahasiswa(nama_file, buka_data)
#print("data mahasiswa berhasil disimpan ke file.") 

# ===========================================================
# Praktikum 2 : Konsep ADT dan file handling (Studi Kasus)
# Latihan 6 : Membuat Menu
# ===========================================================
def main():
    # Menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)
    # MEMPERBAIKI: while True harus menjorok ke dalam (indentasi) fungsi main
    while True:
        print("\n===Menu program=== ")
        print("1. Tampilkan data mahasiswa")
        print("2. Cari data mahasiswa")
        print("3. Update nilai mahasiswa")
        print("4. Simpan data ke file")
        print("0. Keluar")
        pilihan = input("masukkan pilihan (0-4): ").strip()
        if pilihan == '1':
            tampilkan_data(buka_data)  
        elif pilihan == '2':
            cari_data(buka_data)
        elif pilihan == '3':
            update_nilai(buka_data)
        elif pilihan == '4':
            simpan_data_mahasiswa(nama_file, buka_data)
            print("data mahasiswa berhasil disimpan ke file.")
        elif pilihan == '0':
            print("program selesai.")
            break
        else:
            print("pilihan tidak valid. silakan coba lagi.")

if __name__ == "__main__":
    main()