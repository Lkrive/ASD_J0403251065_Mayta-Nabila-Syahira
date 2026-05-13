# ==============================================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
# Materi  : Latihan 2 - Implementasi Algoritma Prim
# ==============================================================================

import heapq

from asyncio import graph

def prim_mst(graph, start_node):
    mst = []           # Menyimpan edge yang terpilih masuk MST
    visited = {start_node} # Menandai node yang sudah terhubung
    edges = [
        (weight, start_node, to_node) 
        for to_node, weight in graph[start_node]
    ]
    heapq.heapify(edges) # Menggunakan priority queue (min-heap) untuk mencari bobot terkecil
    total_weight = 0

    while edges:
        # Ambil edge dengan bobot paling minimum yang terhubung dengan node visited
        weight, u, v = heapq.heappop(edges)
        
        if v not in visited:
            visited.add(v) # Tandai node tujuan sebagai visited
            mst.append((u, v, weight))
            total_weight += weight
            
            # Tambahkan semua edge dari node yang baru dikunjungi ke heap
            for next_node, next_weight in graph[v]:
                if next_node not in visited:
                    heapq.heappush(edges, (next_weight, v, next_node))
    
    return mst, total_weight

# Eksekusi program
mst_result, total = prim_mst(graph, 'A')
print("Edges dalam MST (Prim):", mst_result)
print("Total Bobot Minimum:", total)

# Penjelasan: Prim mulai dari satu node dan secara rakus (greedy) menambah 
# node terdekat yang belum dikunjungi sampai semua node terhubung.

# Pertanyaan Analisis:
# 1. Edge mana yang dipilih pertama kali? 
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
# 3. Berapa total bobot MST yang dihasilkan? 
# 4. Mengapa edge tertentu tidak dipilih?

# Penjelasan & Jawaban:
# 1. Edge yang dipilih pertama kali adalah edge dengan bobot terkecil yang terhubung dengan node awal (dalam kasus ini, edge A-C dengan bobot 2).
# 2. Edge dengan bobot paling kecil dipilih lebih dahulu karena Prim adalah algoritma greedy yang bertujuan untuk membangun MST dengan biaya minimum. Memilih edge terkecil memastikan bahwa kita selalu menambah node dengan biaya paling rendah.
# 3. Total bobot MST yang dihasilkan adalah 7 (A-C = 2, C-D = 1, A-B = 4).
# 4. Edge tertentu tidak dipilih karena mereka akan membentuk siklus atau memiliki bobot yang lebih tinggi dibandingkan dengan edge lain yang tersedia. Misalnya, edge B-D dengan bobot 5 tidak dipilih karena sudah ada edge C-D dengan bobot 1 yang menghubungkan D ke MST dengan biaya lebih rendah. 