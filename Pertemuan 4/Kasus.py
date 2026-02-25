#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

#============================================================
#Studi kasus: Sistem Antrian Layanan Akademik
#Implementasi Queue =>
#Enqueue : memindahkan pointer rear (nambah data baru dari belakang)
#Dequeue : memindahkan pointer front (menghapus data dari depan) 
# Stack ==> Front-> C ->B -> A   None
# Front-> A -> B -> C -> Rear
#============================================================

#1) Mendefinisikan Node (Unit dasar linkedlist)
class Node:
   def __init__(self,nim,nama):
     self.nim = nim #menyimpan nim mahasiswa
     self.nama = nama #menyimpan nama mahasiswa
     self.next = None #pointer node berikutnya (awal)

#2) Mendefinisikan queueu, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
      self.front = None
      self.rear = None

    def is_empty(self):
       #Ketika queue kosong maka front = rear = none
       return self.front is None
    
    #menambahkan data baru ke bagian belakang (rear) => menambahkan antrian mahasiwa yang akan mengajukan layanan
    def enqueue(self,nim,nama):
       nodeBaru = Node(nim,nama)
       #Jika data baru masuk dari queue yang kosong maka data baru = front = rear 
       if self.is_empty():
          self.front = nodeBaru
          self.rear = nodeBaru
          return
       #Jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
       self.rear.next = nodeBaru
       self.rear = nodeBaru
    
    #menghapus data paling depan (memberi layanan akademik)
    def dequeue(self):
       
       if self.is_empty():
          print("Antrian Kosong. Tidak ada Mahasiwa yang dilayani")
          return None
       
       #lihat data bagian front, simpan di variabel data yang akan dihapus (dilayani)
       node_dilayani = self.front
       
       #geser pointer front ke next front
       self.front = self.front.next

       #Jika front menjadi none (data antrian terakhir yang dlayani), maka front = rear = none
       if self.front is None:
         self.rear = None

       return node_dilayani
    
def tampilkan(self):
   if self.is_empty():
            print("Antrian Kosong.")
            return

   print("Daftar Antrian Mahasiswa (Front -> Rear):  ")
   current = self.front
   no = 1
   while current is not None:
      print(f"{no}.{current.nim}- {current.nama}")
      current = current.next
      no += 1
   print()

#Program Utama
def main():
   #Instantiasi queue
   q = queueAkademik()

   while True:
      print("====Sistem Antrian Akademik =====")
      print("1. Tambah Mahasiswa")
      print("2. Layani Mahasiwa")
      print("3. Lihat Antrian")
      print("4. Keluar")

      pilihan = input("Pilih Menu (1-4): ")
      if pilihan == "1":
         nim = input("Masukan Nim: ").strip()
         nama = input("Masukan Nama: ").strip()

         q.enqueue(nim,nama)
         print("Mahasiswa Berhasil Ditambahkan ke Antrian")

      elif pilihan == "2":
         dilayani = q.dequeue()
         print(f"Mahasiswa Dilayani : {dilayani.nim} - {dilayani.nama} ")

      elif pilihan == "3":
         q.tampilkan()

      elif pilihan =="4":
         print("Program Sudah Selesai. Terimakasih")
         break
      else:
         print("Pilihan tidak valid. Silahkan coba lagi 1-4 ")

if __name__ == "__main__":
   main()