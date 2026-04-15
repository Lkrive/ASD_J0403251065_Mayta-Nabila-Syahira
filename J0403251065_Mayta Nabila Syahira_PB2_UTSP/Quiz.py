# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1)
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca data dari file teks dan menyimpannya ke Dictionary.
    Dictionary dipilih karena memiliki kecepatan akses data (search) yang tinggi menggunakan Key.
    """
    database_buku = {}
    try:
        # Membuka file dengan mode 'r' (read)
        with open(nama_file, 'r') as f:
            for baris in f:
                # .strip() menghapus spasi/newline, .split(',') memecah string menjadi list
                data = baris.strip().split(',')
                # Memastikan satu baris memiliki 3 komponen: kode, judul, dan harga
                if len(data) == 3:
                    kode, judul, harga = data
                    # Memasukkan ke dictionary dengan kode_buku sebagai KEY
                    # Harga diubah ke integer agar bisa diolah secara numerik
                    database_buku[kode] = [judul, int(harga)]
    except FileNotFoundError:
        # Penanganan error jika file buku.txt tidak ditemukan di direktori
        print(f"File {nama_file} nggak ketemu di folder ini!")
    return database_buku

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2)
class Node:
    """Kelas untuk merepresentasikan elemen tunggal dalam Linked List"""
    def __init__(self, judul):
        self.judul = judul  # Menyimpan data judul buku
        self.next = None    # Pointer ke node selanjutnya, defaultnya kosong (None)

class LinkedListPromosi:
    """Struktur data Linked List untuk mengelola daftar promosi secara dinamis"""
    def __init__(self):
         self.head = None   # Titik awal Linked List

    def tambah_buku_promosi(self, judul):
        """Menambahkan node baru di akhir daftar (Insert Last)"""
        baru = Node(judul)
        # Jika list kosong, node baru langsung menjadi head
        if not self.head:
            self.head = baru
            return
        # Jika tidak kosong, cari node terakhir (yang .next-nya None)
        curr = self.head
        while curr.next:
            curr = curr.next
        # Sambungkan node terakhir ke node baru
        curr.next = baru

    def tampilkan_promosi(self):
        """Menampilkan seluruh isi Linked List (Traversal)"""
        if not self.head:
            print("Promo kosong.")
            return
        curr = self.head
        print("Buku Promo:", end=" ")
        # Telusuri setiap node sampai ke ujung
        while curr:
            print(f"[{curr.judul}]", end=" -> " if curr.next else "\n")
            curr = curr.next



# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3)
class AntreanKasir:
    """Implementasi antrean menggunakan prinsip FIFO (First In, First Out)"""
    def __init__(self):
        # Menggunakan List Python untuk menampung elemen antrean
        self.antrean = []

    def tambah_antrean(self, nama_pelanggan):
        """Proses Enqueue: Menambahkan elemen ke posisi paling belakang"""
        self.antrean.append(nama_pelanggan)
        print(f"{nama_pelanggan} antre.")

    def layani_pelanggan(self):
        """Proses Dequeue: Mengambil elemen dari posisi paling depan (index 0)"""
        if self.antrean:
            # .pop(0) memastikan elemen yang pertama kali masuk adalah yang pertama keluar
            siapa = self.antrean.pop(0)
            print(f"Melayani: {siapa}")
        else:
            print("Gak ada antrean.")



# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4)
def urutkan_transaksi(list_harga):
    """
    Algoritma Insertion Sort: Mengurutkan data dengan cara menyisipkan elemen 
    ke posisi yang tepat satu per satu (seperti mengurutkan kartu).
    """
    # Dimulai dari indeks 1 karena elemen pertama dianggap sudah terurut
    for i in range(1, len(list_harga)):
        key = list_harga[i]  # Elemen yang akan disisipkan
        j = i - 1
        # Shifting: Menggeser elemen yang lebih besar ke kanan untuk memberi ruang bagi 'key'
        while j >= 0 and list_harga[j] > key:
            list_harga[j+1] = list_harga[j]
            j -= 1
        # Menyisipkan 'key' pada posisi yang sudah benar
        list_harga[j+1] = key
    return list_harga



# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi awal data dan struktur data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db) # Load data dari file ke dictionary
    list_promosi = LinkedListPromosi()   # Inisialisasi Linked List
    antrean_toko = AntreanKasir()        # Inisialisasi Queue
    # Data dummy riwayat transaksi untuk di-sorting
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    # Perulangan menu utama
    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            # Menampilkan isi dictionary yang dibaca dari file
            print("\nKatalog Buku:", data_buku)
        
        elif pilihan == '2':
            # Manajemen Linked List: Input judul baru dan tampilkan list
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            # Manajemen Queue: Memilih antara menambah antrean atau melayani pelanggan
            sub = input("A: Tambah Antrean, B: Layani Pelanggan: ").lower()
            if sub == 'a':
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)
            else:
                antrean_toko.layani_pelanggan()

        elif pilihan == '4':
            # Proses Sorting: Menampilkan data sebelum dan sesudah urut
            print("Harga Sebelum Urut:", riwayat_transaksi)
            # .copy() digunakan agar data asli riwayat_transaksi tidak berubah secara permanen
            hasil_sort = urutkan_transaksi(riwayat_transaksi.copy())
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            # Menutup aplikasi
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()