#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Materi 2 : BFS (Breadth-First Search) pada Graph
#===============================================================

# Struktur data untuk membuat antrian, kita gunakan dari library collections bawaan Python
from collections import deque

# Representasi graph sebagai adjacency list
# Graph ini berbentuk tree (pohon) dengan A sebagai root
graph = {
    'A': ['B', 'C'],    # Level 1: A terhubung ke B dan C
    'B': ['D', 'E'],    # Level 2: B terhubung ke D dan E
    'C': ['F', 'G'],    # Level 2: C terhubung ke F dan G
    'D': [],            # Level 3: D tidak punya tetangga (daun)
    'E': [],            # Level 3: E tidak punya tetangga (daun)
    'F': [],            # Level 3: F tidak punya tetangga (daun)
    'G': []             # Level 3: G tidak punya tetangga (daun)
}

def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran BFS pada graph
    # graph: dictionary yang menyimpan struktur dari graph
    # start: node awal untuk memulai BFS

    # Queue digunakan untuk menyimpan node yang akan diproses/dibaca
    queue = deque()
    # Visited set digunakan untuk melacak node yang sudah dikunjungi/diproses
    visited = set()

    # Masukkan node awal ke queue
    queue.append(start)
    # Tandai node awal sebagai sudah dikunjungi
    visited.add(start)

    while queue:
        # Mengambil node paling depan dari queue untuk diproses (FIFO)
        node = queue.popleft()
        # Menampilkan node yang sedang dikunjungi
        print("Mengunjungi node:", node)

        # Periksa setiap tetangga dari node yang sedang diproses
        for neighbor in graph[node]:
            # Jika tetangga belum dikunjungi
            if neighbor not in visited:
                # Tandai tetangga sebagai sudah dikunjungi
                visited.add(neighbor)
                # Masukkan tetangga ke dalam queue untuk diproses selanjutnya
                queue.append(neighbor)

# Memanggil fungsi BFS dengan graph dan node awal 'A'
bfs(graph, "A")