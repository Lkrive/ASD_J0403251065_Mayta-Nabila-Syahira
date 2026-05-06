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
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh 2 menit, karena itu jarak paling kecil dibanding yang lain.
# 2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit lewat jalur Gerbang -> Kantin -> Lab -> Aula (2 + 4 + 1 = 7).
# 3. Jalur langsung tidak selalu paling cepat, karena yang dihitung itu total bobotnya. Bisa aja jalur lebih panjang tapi tiap bagiannya kecil, jadi totalnya malah lebih cepat.
# 4. Dijkstra cocok dipakai di kasus ini karena semua bobotnya positif (waktu tempuh), dan algoritma ini memang dibuat untuk nyari jalur tercepat dengan efisien.