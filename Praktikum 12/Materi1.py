#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Materi 1 : Algoritma Dijkstra
#===============================================================

import heapq  # dipakai untuk priority queue (ambil jarak terkecil dulu)

graph = { 
    'A': {'B': 4, 'C': 2},   # dari A ke B = 4, A ke C = 2
    'B': {'D': 5},           # dari B ke D = 5
    'C': {'D': 1},           # dari C ke D = 1
    'D': {}                  # D tidak punya tetangga
} 

def dijkstra(graph, start): 
    # Menyimpan jarak minimum ke semua node
    distances = {node: float('inf') for node in graph}  # awalnya semua ∞ (belum diketahui)
 
    # Jarak node awal = 0 (karena ke dirinya sendiri)
    distances[start] = 0 
 
    # Priority queue (jarak, node)
    pq = [(0, start)]  # mulai dari node awal
 
    while pq: 
        # Ambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(pq) 
 
        # Periksa semua tetangga dari node sekarang
        for neighbor, weight in graph[current_node].items(): 
 
            distance = current_distance + weight  # hitung jarak lewat node ini
 
            # Kalau jarak baru lebih kecil → update
            if distance < distances[neighbor]: 
 
                distances[neighbor] = distance  # simpan jarak baru
 
                heapq.heappush(pq, (distance, neighbor))  # masukkan ke antrian lagi
 
    return distances  # hasil akhir semua jarak
 
# Jalankan dari node A
hasil = dijkstra(graph, 'A') 

print(hasil)  # tampilkan hasil