#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Materi 2 : BFS (Breadth-First Search) pada Graph
#===============================================================

#struktru data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque
from collections import deque
#representasi graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(graph, start):
    #Fungsi untuk melakukan penelusuran BFS pada graph
    #graph: dictionary yang menyimpan struktur dari graph
    #start: node awal untuk memulai BFS

    #Queue digunakan untuk menyimpan ode yang akan diproses/dibaca
    queue = deque()
    #Visited set digunakan untuk melacak node yang sudah dikunjungi/diproses
    visited = set()
    #masukkan node awal ke queue
    queue.append(start)
    #tandai node awal sebagai sudah dikunjungi
    visited.add(start)

    while queue:
        #mengambil node paling depan dari queue untuk diproses
        node = queue.popleft()
        #menampilkan node yang sedang dikunjungi
        print("Mengunjungi node:", node) 
        #periksa setiap tetangga dari node yang sedang diproses
        for neighbor in graph[node]:
            #jika tetangga belum dikunjungi
            if neighbor not in visited:
                #tandai tetangga sebagai sudah dikunjungi
                visited.add(neighbor)
                #masukkan tetangga ke dalam queue untuk diproses selanjutnya
                queue.append(neighbor)
#memanggil fungsi BFS dengan graph dan node awal 'A'
bfs(graph, "A")