#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Materi 1 : Dasar Graph
#===============================================================

# Graph direpresentasikan sebagai adjacency list menggunakan dictionary
# Setiap key adalah node (simpul), dan value-nya adalah list node yang terhubung langsung
# Graph ini bersifat undirected (tidak berarah), karena setiap koneksi dicatat di kedua sisi
graph = {
    'A': ['B', 'C'],    # A terhubung ke B dan C
    'B': ['A', 'D'],    # B terhubung ke A dan D
    'C': ['A', 'D'],    # C terhubung ke A dan D
    'D': ['B', 'C']     # D terhubung ke B dan C
}

# Iterasi setiap node dalam graph dan tampilkan daftar tetangganya
# Ini disebut adjacency list — cara paling umum merepresentasikan graph di Python
for node in graph:
    print(node, "=>", graph[node])