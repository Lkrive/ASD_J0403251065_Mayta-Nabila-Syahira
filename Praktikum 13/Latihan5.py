# ==============================================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
# Materi  : Latihan 5 - Studi Kasus Jaringan Router
# ==============================================================================

# Kasus 2: Jaringan Router (Representasi Edges untuk Kruskal)
nodes_router = ['RouterA', 'RouterB', 'RouterC', 'RouterD']
edges_router = [
    ('RouterA', 'RouterB', 3),
    ('RouterA', 'RouterC', 2),
    ('RouterB', 'RouterD', 5),
    ('RouterC', 'RouterD', 1),
    ('RouterB', 'RouterC', 4)
]

# Menggunakan logika Kruskal untuk mencari MST koneksi antar router
def kruskal_router(nodes, edges):
    edges.sort(key=lambda x: x[2])
    parent = {n: n for n in nodes}
    
    def find(i):
        if parent[i] == i: return i
        return find(parent[i])

    mst, total = [], 0
    for u, v, w in edges:
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_u] = root_v
            mst.append(f"{u} <-> {v} [Latency: {w}]")
            total += w
    return mst, total

mst_res, total_lat = kruskal_router(nodes_router, edges_router)

print("Koneksi Router Teroptimal (MST):")
for k in mst_res:
    print(k)
print(f"Total Latency Minimum: {total_lat}")

# Analisis: MST memastikan semua router terhubung dengan total latency terkecil 
# tanpa ada loop yang bisa menyebabkan paket data berputar (broadcast storm).

# Pertanyaan Analisis:
# 1. Kasus apa yang dipilih? 
# 2. Algoritma apa yang digunakan? 
# 3. Edge mana saja yang dipilih dalam MST? 
# 4. Berapa total bobot MST? 
# 5. Mengapa edge tertentu tidak dipilih?

# Penjelasan & Jawaban:
# 1. Kasus yang dipilih adalah jaringan router, di mana kita ingin menghubungkan beberapa router dengan latency minimum.
# 2. Algoritma yang digunakan adalah Kruskal, yang mengurutkan edge berdasarkan bobot (latency) dan memilih edge terkecil yang tidak membentuk siklus.
# 3. Edge yang dipilih dalam MST adalah: RouterC-RouterD (1), RouterA-RouterC (2), RouterA-RouterB (3).
# 4. Total bobot MST adalah 6 (1 + 2 + 3).
# 5. Edge tertentu tidak dipilih karena mereka akan membentuk siklus atau memiliki bobot yang lebih tinggi dibandingkan dengan edge lain yang tersedia. Misalnya, edge RouterB-RouterD dengan bobot 5 tidak dipilih karena sudah ada edge RouterC-RouterD dengan bobot 1 yang menghubungkan D ke MST dengan latency lebih rendah, dan edge RouterB-RouterC dengan bobot 4 tidak dipilih karena sudah ada edge RouterA-RouterC dengan bobot 2 yang menghubungkan C ke MST dengan latency lebih rendah.