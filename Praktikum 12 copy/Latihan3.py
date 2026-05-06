#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 3 : Implementasi Bellman-Ford
#===============================================================

# Weighted graph dengan bobot negatif
graph = {
 'A': {'B': 5, 'C': 4},
 'B': {},
 'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika ditemukan jarak yang lebih kecil → update
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 

    # return harus di luar loop
    return distances
       
hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)
    
# Pertanyaan Analisis:
# 1. Berapa bobot langsung dari A ke B?
# 2. Berapa total bobot jalur A -> C -> B?
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# 5. Apa yang dimaksud dengan proses relaksasi edge?
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?

# Penjelasan & Jawaban:
# 1. Bobot langsung dari A ke B adalah 5, karena langsung terhubung dari A ke B.
# 2. Total bobot jalur A -> C -> B adalah 4 (A ke C) + (-2) (C ke B) = 2, jadi lebih kecil.
# 3. Jalur A -> C -> B menghasilkan jarak lebih kecil, yaitu 2, dibandingkan jalur langsung A -> B yang nilainya 5.
# 4. Bellman-Ford bisa digunakan untuk bobot negatif karena dia ngecek semua kemungkinan jalur berulang kali, jadi kalau ada perubahan jarak akibat bobot negatif masih bisa diperbaiki.
# 5. Relaksasi edge itu proses ngecek apakah jarak ke suatu node bisa diperkecil lewat node lain, kalau bisa maka jaraknya di-update.
# 6. Perbedaan utama Bellman-Ford dan Dijkstra adalah Bellman-Ford bisa menangani bobot negatif, sedangkan Dijkstra tidak, karena Dijkstra pakai pendekatan greedy yang bisa salah kalau ada nilai negatif.