#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 5 : Studi kasus dengan Program Shortest Path
# Algoritma : Dijkstra
#===============================================================

import heapq

graph = {
    'Bogor':   [('Jakarta', 5), ('Depok', 2)],
    'Depok':   [('Jakarta', 2), ('Bandung', 6)],
    'Jakarta': [('Bandung', 7)],
    'Bandung': []
}

def dijkstra(graph, node_awal):
    jarak = {kota: float('inf') for kota in graph}
    jarak[node_awal] = 0
 
    antrian = [(0, node_awal)]
 
    sebelumnya = {kota: None for kota in graph}
 
    while antrian:
        jarak_kini, kota_kini = heapq.heappop(antrian)
 
        if jarak_kini > jarak[kota_kini]:
            continue
 
        for tetangga, bobot in graph[kota_kini]:
            jarak_baru = jarak[kota_kini] + bobot
 
            if jarak_baru < jarak[tetangga]:
                jarak[tetangga] = jarak_baru
                sebelumnya[tetangga] = kota_kini
                heapq.heappush(antrian, (jarak_baru, tetangga))
 
    return jarak, sebelumnya


node_awal = 'Bogor'

# 🔥 INI YANG KURANG TADI
hasil_jarak, hasil_jalur = dijkstra(graph, node_awal)


print(f"Jarak terpendek dari {node_awal}:")
print("-" * 30)
 
for kota, jarak in hasil_jarak.items():
    if jarak == float('inf'):
        print(f"{node_awal} -> {kota} = tidak terjangkau")
    else:
        print(f"{node_awal} -> {kota} = {jarak}")

print("\nDetail rute:")
print("-" * 30)
 
def rekonstruksi_jalur(sebelumnya, node_awal, node_tujuan):
    jalur = []
    kota = node_tujuan
    while kota is not None:
        jalur.append(kota)
        kota = sebelumnya[kota]
    jalur.reverse()

    if jalur[0] == node_awal:
        return " -> ".join(jalur)
    return "tidak terjangkau"
 
for kota in hasil_jarak:
    rute = rekonstruksi_jalur(hasil_jalur, node_awal, kota)
    print(f"Rute ke {kota}: {rute} (jarak: {hasil_jarak[kota]})")


# Pertanyaan Analisis:
# 1. Node awal yang digunakan apa?
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.

# Penjelasan & Jawaban:
# 1. Node awal yang digunakan adalah 'A'.
# 2. Node yang memiliki jarak paling kecil dari node awal adalah 'C' dengan jarak 2.
# 3. Node yang memiliki jarak paling besar dari node awal adalah 'D' dengan jarak 3.
# 4. Algoritma Dijkstra bekerja dengan cara memulai dari node awal (A) dan mengunjungi 
#    node tetangga yang memiliki jarak terkecil terlebih dahulu. Dalam kasus ini, algoritma 
#    pertama kali mengunjungi node C karena memiliki jarak 2, kemudian mengunjungi node B dengan jarak 4, 
#    dan terakhir mengunjungi node D dengan jarak 3. Algoritma terus memperbarui jarak ke setiap node 
#    berdasarkan bobot edge yang dilalui, sehingga menghasilkan jarak terpendek dari node awal ke semua node lainnya.
