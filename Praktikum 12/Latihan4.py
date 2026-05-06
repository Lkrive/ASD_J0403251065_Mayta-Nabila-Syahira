#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 4 : Studi kasus jalur terpendek Lokasi Kampus 
# Algoritma : Dijkstra
#===============================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Pertanyaan Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?

# Penjelasan & Jawaban:
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh
#    2 menit.
# 2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit melalui jalur
#    Gerbang -> Kantin -> Lab -> Aula (2 + 4 + 1 = 7 menit).
# 3. Jalur langsung tidak selalu menghasilkan jarak paling kecil karena bobot
#    pada setiap edge bisa berbeda. Dalam kasus ini, meskipun ada jalur langsung
#    dari Gerbang ke Aula, jalur tersebut memiliki bobot yang lebih besar dibandingkan
#    dengan jalur melalui Kantin dan Lab. Oleh karena itu, penting untuk mempertimbangkan
#    bobot pada setiap edge dalam menentukan jalur terpendek, bukan hanya jumlah edge.
# 4. Dijkstra cocok digunakan pada kasus lokasi kampus ini karena algoritma ini
#    dirancang untuk menemukan jalur terpendek dalam graph dengan bobot non-negatif
#    seperti waktu tempuh. Dijkstra efisien dalam menangani graph yang tidak terlalu besar
#    dan memberikan hasil yang akurat untuk kasus ini.


