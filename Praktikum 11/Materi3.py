#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Materi 3 : Implementasi DFS (Depth-First Search) pada Graph
#===============================================================

# Representasi graph menggunakan adjacency list
# Catatan: node 'G' tidak terhubung ke node manapun dan tidak bisa dicapai dari 'A'
graph = {
    'A': ['B', 'C'],    # A terhubung ke B dan C
    'B': ['D', 'E'],    # B terhubung ke D dan E
    'C': ['F'],         # C terhubung ke F
    'D': [],            # D tidak punya tetangga (daun)
    'E': [],            # E tidak punya tetangga (daun)
    'F': [],            # F tidak punya tetangga (daun)
    'G': []             # G tidak punya tetangga dan terisolasi (tidak terhubung ke node lain)
}

def dfs(graph, node, visited):
    # Fungsi untuk melakukan penelusuran graph dengan metode DFS
    # graph   : dictionary yang menyimpan struktur dari graph
    # node    : node yang sedang dikunjungi
    # visited : set yang menyimpan node yang sudah dikunjungi

    # Tandai node ini sebagai node yang sudah dikunjungi
    visited.add(node)

    # Tampilkan node yang sedang dikunjungi
    print(node, end=' ')

    # Periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:        # Iterasi untuk setiap tetangga dari node
        # Jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            # Melakukan DFS secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

# Set kosong untuk menyimpan node yang sudah dikunjungi
visited = set()

# Menjalankan DFS dari node A
print("Urutan DFS:")
dfs(graph, 'A', visited)