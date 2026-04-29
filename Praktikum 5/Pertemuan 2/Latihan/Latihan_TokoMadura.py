# ========================================================
# Tugas 8.1: Sistem Stok Warung Madura 24 Jam
# Nama: Mayta Nabila Syahira
# Jurusan: Teknologi Rekayasa Perangkat Lunak (TPL)
# ========================================================

# Nama file didefinisikan secara global agar konsisten
nama_file = "data_warung.txt"

def baca_stok(nama_file):
    data_warung = {}
    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                baris = baris.strip()
                if baris:
                    # Memisahkan data berdasarkan koma
                    kode, nama, stok = baris.split(',')
                    data_warung[kode] = {'nama': nama, 'stok': int(stok)}
    except FileNotFoundError:
        # Jika file belum ada (misal: baru pertama kali dijalankan)
        print(f"[!] File {nama_file} belum tersedia. Data baru akan dibuat saat disimpan.")
    return data_warung

def tampilkan_barang(data_dict):
    if not data_dict:
        print("\n[!] Warung kosong, belum ada stok tercatat.")
        return
    
    print("\n" + "="*45)
    print(f"{'KODE':<8} | {'NAMA BARANG':<20} | {'STOK':>5}")
    print("-" * 45)
    # Menampilkan data yang diurutkan berdasarkan Kode Barang
    for kode in sorted(data_dict.keys()):
        item = data_dict[kode]
        print(f"{kode:<8} | {item['nama']:<20} | {item['stok']:>5}")
    print("="*45)

def cari_barang(data_dict):
    kode = input("\nMasukkan Kode Barang yang dicari: ").strip().upper()
    if kode in data_dict:
        item = data_dict[kode]
        print(f"-> DATA Ditemukan!")
        print(f"   Nama Barang : {item['nama']}")
        print(f"   Jumlah Stok : {item['stok']}")
    else:
        print("-> [!] Barang tidak ditemukan.")

def tambah_barang(data_dict):
    kode = input("\nInput Kode Barang Baru: ").strip().upper()
    if kode in data_dict:
        print("-> [!] Kode sudah digunakan. Gunakan menu Update untuk tambah stok.")
        return
    
    nama = input("Nama Barang (Gunakan_Underscore): ").strip()
    try:
        stok_awal = int(input("Jumlah Stok Awal: "))
        data_dict[kode] = {'nama': nama, 'stok': max(0, stok_awal)}
        print(f"-> Sukses! {nama} telah ditambahkan.")
    except ValueError:
        print("-> [!] Gagal! Stok harus berupa angka bulat.")

def update_stok(data_dict):
    kode = input("\nMasukkan Kode Barang yang akan diupdate: ").strip().upper()
    if kode not in data_dict:
        print("-> [!] Barang tidak ditemukan.")
        return
    
    print(f"\nBarang: {data_dict[kode]['nama']} (Stok saat ini: {data_dict[kode]['stok']})")
    print("1. Tambah Stok (Barang Masuk)")
    print("2. Kurangi Stok (Barang Terjual)")
    opsi = input("Pilih aksi (1/2): ")
    
    try:
        jumlah = int(input("Masukkan jumlah barang: "))
        if opsi == '1':
            data_dict[kode]['stok'] += jumlah
            print("-> Update Berhasil: Stok bertambah.")
        elif opsi == '2':
            if data_dict[kode]['stok'] - jumlah < 0:
                print("-> [!] Gagal! Stok tidak boleh negatif.")
            else:
                data_dict[kode]['stok'] -= jumlah
                print("-> Update Berhasil: Stok berkurang.")
        else:
            print("-> [!] Pilihan menu update tidak valid.")
    except ValueError:
        print("-> [!] Input jumlah harus berupa angka.")

def simpan_ke_file(nama_file, data_dict):
    try:
        with open(nama_file, 'w') as file:
            for kode, info in data_dict.items():
                file.write(f"{kode},{info['nama']},{info['stok']}\n")
        print(f"-> Berhasil menyimpan semua data ke '{nama_file}'.")
    except Exception as e:
        print(f"-> [!] Terjadi kesalahan saat menyimpan: {e}")

def main():
    # Inisialisasi: Load data dari file ke memory (dictionary)
    stok_warung = baca_stok(nama_file)
    
    while True:
        print("\n=== SISTEM MANAJEMEN STOK WARUNG MADURA ===")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang Berdasarkan Kode")
        print("3. Tambah Jenis Barang Baru")
        print("4. Update Jumlah Stok")
        print("5. Simpan Perubahan ke File")
        print("0. Keluar")
        
        pilihan = input("Masukkan pilihan (0-5): ").strip()
        
        if pilihan == '1':
            tampilkan_barang(stok_warung)
        elif pilihan == '2':
            cari_barang(stok_warung)
        elif pilihan == '3':
            tambah_barang(stok_warung)
        elif pilihan == '4':
            update_stok(stok_warung)
        elif pilihan == '5':
            simpan_ke_file(nama_file, stok_warung)
        elif pilihan == '0':
            print("\nProgram selesai. Warung Madura tetap buka 24 jam!")
            break
        else:
            print("-> [!] Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()