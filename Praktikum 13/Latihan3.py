# ==============================================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
# Materi  : Latihan 3 - Implementasi Algoritma Kruskal
# ==============================================================================

class DisjointSet:
    # Digunakan untuk mengecek apakah dua node berada dalam komponen yang sama (mencegah cycle)
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

def kruskal_mst(nodes, edges):
    mst = []
    # Urutkan semua edge berdasarkan bobot dari terkecil ke terbesar
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(nodes)
    total_weight = 0

    for u, v, weight in edges:
        # Jika node u dan v belum terhubung (tidak membentuk cycle), ambil edge-nya
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            
    return mst, total_weight

# Data Edges (u, v, weight)
all_edges = [
    ('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1), ('B', 'D', 5),
    ('C', 'D', 8), ('C', 'E', 10), ('D', 'E', 2), ('D', 'Z', 6), ('E', 'Z', 3)
]
nodes_list = ['A', 'B', 'C', 'D', 'E', 'Z']

mst_k, weight_k = kruskal_mst(nodes_list, all_edges)
print("Edges dalam MST (Kruskal):", mst_k)
print("Total Bobot Minimum:", weight_k)

# Penjelasan: Kruskal mengurutkan seluruh edge di awal dan mengambil yang terkecil 
# satu per satu asalkan tidak membentuk siklus (cycle).

# Pertanyaan Analisis:
# 1. Node awal apa yang digunakan? 
# 2. Edge mana yang dipilih pertama kali? 
# 3. Bagaimana Prim menentukan edge berikutnya? 
# 4. Berapa total bobot MST yang dihasilkan? 
# 5. Apa perbedaan pendekatan Prim dan Kruskal?

# Penjelasan & Jawaban:
# 1. Kruskal tidak memulai dari node tertentu, melainkan mengurutkan semua edge terlebih dahulu. Namun, edge pertama yang dipilih adalah edge dengan bobot terkecil (B-C dengan bobot 1).
# 2. Edge yang dipilih pertama kali adalah edge dengan bobot terkecil, yaitu edge B-C dengan bobot 1.
# 3. Prim menentukan edge berikutnya dengan memilih edge terkecil yang terhubung dengan node yang sudah terhubung (visited), sedangkan Kruskal memilih edge terkecil dari seluruh edge yang tersedia tanpa memperhatikan node mana yang sudah terhubung.
# 4. Total bobot MST yang dihasilkan adalah 10 (B-C = 1, D-E = 2, A-C = 2, E-Z = 3, D-Z = 6).
# 5. Perbedaan pendekatan Prim dan Kruskal adalah Prim membangun MST dengan memulai dari satu node dan menambahkan edge terkecil yang terhubung dengan node yang sudah terhubung, sedangkan Kruskal mengurutkan semua edge terlebih dahulu dan memilih edge terkecil yang tidak membentuk siklus tanpa memperhatikan node mana yang sudah terhubung.    