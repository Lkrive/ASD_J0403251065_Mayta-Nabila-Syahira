# ==============================================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
# Materi  : Latihan 4 - Studi Kasus Jaringan Jalan (MST)
# ==============================================================================

# Kasus 1: Jaringan Jalan Antar Kota (Weighted Graph)
jaringan_kota = {
    'Bogor': [('Jakarta', 5), ('Depok', 2)],
    'Jakarta': [('Bogor', 5), ('Depok', 3), ('Bandung', 6)],
    'Depok': [('Bogor', 2), ('Jakarta', 3), ('Bandung', 4)],
    'Bandung': [('Jakarta', 6), ('Depok', 4)]
}

# Menggunakan fungsi Prim dari latihan sebelumnya untuk mencari MST
import heapq
def prim_kota(graph, start):
    mst, total = [], 0
    visited = {start}
    edges = [(w, start, to) for to, w in graph[start]]
    heapq.heapify(edges)

    while edges:
        w, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append(f"{u} - {v} (Biaya: {w})")
            total += w
            for nxt, nxt_w in graph[v]:
                if nxt not in visited:
                    heapq.heappush(edges, (nxt_w, v, nxt))
    return mst, total

hasil, total_biaya = prim_kota(jaringan_kota, 'Bogor')

print("Rute Pembangunan Jalan Minimum:")
for rute in hasil:
    print(rute)
print(f"Total Biaya Minimum: {total_biaya}")

# Analisis: Rute ini menghubungkan semua kota dengan biaya kabel/jalan paling hemat.

# Pertanyaan Analisis:
# 1. Algoritma apa yang digunakan? 
# 2. Edge mana saja yang dipilih? 
# 3. Berapa total biaya minimum? 
# 4. Mengapa MST cocok digunakan pada kasus ini? 

# Penjelasan & Jawaban:
# 1. Algoritma yang digunakan adalah Prim, yang merupakan algoritma greedy untuk menemukan Minimum Spanning Tree (MST).
# 2. Edge yang dipilih adalah: Bogor-Depok (2), Depok-Jakarta (3), Depok-Bandung (4).
# 3. Total biaya minimum adalah 9 (2 + 3 + 4).
# 4. MST cocok digunakan pada kasus ini karena kita ingin menghubungkan semua kota dengan biaya minimum tanpa membentuk 
#    siklus, yang merupakan karakteristik utama dari MST. Dengan menggunakan MST, kita dapat memastikan bahwa semua kota 
#    terhubung dengan biaya paling efisien.