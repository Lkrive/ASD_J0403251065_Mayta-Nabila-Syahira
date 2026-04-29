#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

# === LATIHAN 1 ===
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def delete_node(self, key):
        temp = self.head

        # Jika node pertama yang dihapus
        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Jika data tidak ditemukan
        if temp is None:
            print("Data tidak ditemukan")
            return

        prev.next = temp.next


# === BAGIAN PEMBUKTIAN DATA LAT 1 ===
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    print("Data Awal:")
    ll.display()
    
    print("Menghapus node 20...")
    ll.delete_node(20)
    ll.display()

# === LATIHAN 3 ===
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False


# === BAGIAN PEMBUKTIAN DATA LAT 3 ===
if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("Masukkan elemen ke dalam Doubly Linked List: 2, 6, 9, 14, 20")

    for x in [2, 6, 9, 14, 20]:
        dll.insert_at_end(x)

    cari = int(input("Masukkan elemen yang ingin dicari: "))

    if dll.search(cari):
        print(f"Elemen {cari} ditemukan dalam Doubly Linked List.")
    else:
        print(f"Elemen {cari} tidak ditemukan dalam Doubly Linked List.")



# === LATIHAN 5 ===
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null") 
    # === RUMUS REVERSE ===
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next 
            current.next = prev     
            prev = current          
            current = next_node   
        self.head = prev

# === BAGIAN PEMBUKTIAN DATA LAT 5 ===
if __name__ == "__main__":
    ll = LinkedList()
    input_data = [1, 2, 3, 4, 5]
    for x in input_data:
        ll.insert_at_end(x)
    print("Linked List sebelum dibalik:")
    ll.display()
    # Jalankan rumus reverse
    ll.reverse()
    print("Linked List setelah dibalik:")
    ll.display()