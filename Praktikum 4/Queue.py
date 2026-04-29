#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================


#============================================================
#Implementasi Dasar : Queue Berbasis Linked List
#============================================================

# Membuat class Node (merupakan unit dasar dari Linked List)
class Node: #class implementasi stack
    def __init__(self, data): #konstruktor
        self.data = data #menyimpan nilai /data
        self.next = None #pointer ke note berikutnya (awal=none)

#Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None # Node paling kanan
        self.rear = None # Node paling belakang

    def is_empty(self):
        return self.front is None
    
    def enqueue(self,data):
        #menambah data di belakang (rear)
        nodeBaru = Node(data)

        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #Jika queue tidak kosong:
        #Rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        #Rear pindah ke node baru
        self.rear = nodeBaru


    def dequeue(self):
        #menghapus data dari depan 

        #1)lihat data yang paling depan
        data_terhapus = self.front.data

        #2)geser ke front berikutnya
        self.front = self.front.next

        #3) JIka setelah geser front menjadi nine, maka queue kosong
        #rear juga harus jadi none
        if self.front is None:
           self.rear = None

        return data_terhapus

    def tampilkan(self):
        #menampilkan isi queue dari front ke rear
        current = self.front
        print("Front -> ", end="")
        
        while current:
         print(current.data, end=" -> ")
         current = current.next

    print("None <- Rear")


#instantiasi objek class QueueLL
q = QueueLL()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.tampilkan()

q.dequeue()
q.tampilkan()