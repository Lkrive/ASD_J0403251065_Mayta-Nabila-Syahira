#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================


#============================================================
#Implementasi Dasar : NOde pada Linked List
#============================================================

# Membuat class Node (merupakan unit dasar dari Linked List)
class Node:  #class implementasi stack
    def __init__(self, data): #konstruktor
        self.data = data #menyimpan nilai /data
        self.next = None #pointer ke note berikutnya
        
#1) Membuata node satu persatu
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')

#2) Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

#3)  Menentukan node pertama (head)
head = nodeA

#4) Travesal : menelusuri dari head sampai none
current = head
while current is not None :
    print(current.data) # menaampilkan data pad node saat ini
    current = current.next #pindah ke node berikutnya


#============================================================
#implementasi Dasar : Linked List + Insert Awal 
#============================================================

class LinkedList:
    def __init__(self):
        self.head = None #awalnya kosong

    def insert_awal(self,data): #push dalam stack
        #1) buat node baru
        nodeBaru = Node(data) #panggil class node

        #2) node baru menunjuk ke head lama
        nodeBaru.next = self.head

        #3) head pindah ke node baru
        self.head =  nodeBaru

    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        #menggeser head ke node berikutnya
        self.head = self.head.next
        print('Node yang dihapus adalah: ',data_terhapus)

    def tampilkan(self): #implementasi traversal/ menelusuri
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print('===List Baru===')
ll = LinkedList() #instantiasi objek ke class LInked List
ll.insert_awal('X')
ll.insert_awal('Y')
ll.insert_awal('Z')
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()
