# ==========================================================
# Nama: Mayta Nabila Syahira
# NIM: J0403251065
# Kelas: P/B2
# ==========================================================

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

# Class Node sebagai elemen dasar Linked List
class Node:
    def __init__(self, no, nama, servis):
        self.no = no              # menyimpan nomor antrian
        self.nama = nama          # menyimpan nama pelanggan
        self.servis = servis      # menyimpan jenis servis
        self.next = None          # pointer ke node berikutnya


# Class Queue berbasis Linked List
class QueueBengkel:
    def __init__(self):
        self.front = None   # menunjuk ke pelanggan paling depan
        self.rear = None    # menunjuk ke pelanggan paling belakang

    # Method untuk menambahkan pelanggan ke antrian (enqueue)
    def enqueue(self, no, nama, servis):
        nodeBaru = Node(no, nama, servis)  # membuat node baru

        # Jika antrian masih kosong
        if self.front is None:
            self.front = nodeBaru
            self.rear = nodeBaru
        else:
            # rear lama menunjuk ke node baru
            self.rear.next = nodeBaru
            # rear pindah ke node baru
            self.rear = nodeBaru

        print("Pelanggan berhasil ditambahkan ke antrian.")

    # Method untuk melayani pelanggan terdepan (dequeue)
    def dequeue(self):
        # Jika antrian kosong
        if self.front is None:
            print("Antrian kosong. Tidak ada pelanggan untuk dilayani.")
            return

        # Simpan data pelanggan yang akan dilayani
        pelanggan_layani = self.front

        # Geser front ke node berikutnya
        self.front = self.front.next

        # Jika setelah digeser menjadi kosong, rear juga harus None
        if self.front is None:
            self.rear = None

        print("\nMelayani Pelanggan:")
        print("No Antrian :", pelanggan_layani.no)
        print("Nama       :", pelanggan_layani.nama)
        print("Servis     :", pelanggan_layani.servis)

    # Method untuk menampilkan seluruh antrian
    def tampilkan(self):
        # Jika antrian kosong
        if self.front is None:
            print("Antrian masih kosong.")
            return

        print("\nDaftar Antrian Pelanggan:")
        current = self.front

        # Traversal dari front sampai rear
        while current is not None:
            print("---------------------------------")
            print("No Antrian :", current.no)
            print("Nama       :", current.nama)
            print("Servis     :", current.servis)
            current = current.next

        print("---------------------------------")
        print("Front berada di pelanggan pertama.")
        print("Rear berada di pelanggan terakhir.")


# ==========================================================
# Program Utama
# ==========================================================

def main():
    q = QueueBengkel()

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama       : ")
            servis = input("Servis     : ")
            q.enqueue(no, nama, servis)

        elif pilih == "2":
            q.dequeue()

        elif pilih == "3":
            q.tampilkan()

        elif pilih == "4":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid.")


# Menjalankan program
if __name__ == "__main__":
    main()
