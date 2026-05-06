#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 2 : Implementasi Dijkstra
#===============================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
 'A': {'B': 4, 'C': 2},
 'B': {'D': 5},
 'C': {'D': 1},
 'D': {}
}

def dijkstra(graph, start):
 """
 Fungsi untuk mencari jarak terpendek dari node start
 ke seluruh node lain menggunakan algoritma Dijkstra.
 """
 # Semua jarak awal dibuat tak hingga
 distances = {node: float('inf') for node in graph}

 # Jarak dari start ke start adalah 0
 distances[start] = 0

 # Priority queue menyimpan pasangan (jarak, node)
 priority_queue = [(0, start)]

 while priority_queue:
   current_distance, current_node = heapq.heappop(priority_queue)

   # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, skip
   if current_distance > distances[current_node]: 
      continue

   # Periksa semua tetangga dari node saat ini
   for neighbor, weight in graph[current_node].items():
       distance = current_distance + weight

       # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
       if distance < distances[neighbor]:
           distances[neighbor] = distance
           heapq.heappush(priority_queue, (distance, neighbor))

 # return HARUS di luar while
 return distances
 

hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
   print(node, "=", distance)

# Pertanyaan Analisis:
# 1. Berapa jarak terpendek dari A ke B?
# 2. Berapa jarak terpendek dari A ke C?
# 3. Berapa jarak terpendek dari A ke D?
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?

# Penjelasan & Jawaban:
# 1. Jarak terpendek dari A ke B adalah 4.
# 2. Jarak terpendek dari A ke C adalah 2.
# 3. Jarak terpendek dari A ke D adalah 3 (melalui C) dibandingkan dengan 9 (melalui B).
# 4. Jarak A ke D lebih kecil melalui C karena bobot dari A ke C (2) dan C ke D (1) lebih 
#    kecil dibandingkan dengan bobot dari A ke B (4) dan B ke D (5).
# 5. Fungsi priority_queue dalam algoritma Dijkstra adalah untuk menyimpan node-node yang akan 
#    diproses berdasarkan jarak terpendek yang ditemukan sejauh ini. Node dengan jarak terpendek 
# akan diproses terlebih dahulu, sehingga memastikan bahwa algoritma berjalan efisien.
