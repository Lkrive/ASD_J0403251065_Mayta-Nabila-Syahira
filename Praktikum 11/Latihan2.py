#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 2 : Studi Kasus DFS (Eksplorasi Jalur)
#===============================================================

# Representasi graph sebagai adjacency list (dictionary)
# Setiap key adalah node, value-nya adalah list tetangga yang bisa dikunjungi
graph = {
    'A': ['B', 'C'],    # A terhubung ke B dan C
    'B': ['D', 'E'],    # B terhubung ke D dan E
    'C': ['F'],         # C terhubung ke F
    'D': [],            # D tidak punya tetangga (daun)
    'E': [],            # E tidak punya tetangga (daun)
    'F': []             # F tidak punya tetangga (daun)
}

def dfs(graph, node, visited):
    visited.add(node)           # Tandai node saat ini sebagai sudah dikunjungi
    print(node, end=" ")        # Cetak node yang sedang dikunjungi

    for neighbor in graph[node]:        # Iterasi semua tetangga dari node saat ini
        if neighbor not in visited:     # Jika tetangga belum dikunjungi
            dfs(graph, neighbor, visited)   # Rekursi: masuk lebih dalam ke tetangga tersebut

# Inisialisasi set kosong untuk menyimpan node yang sudah dikunjungi
visited = set()

# Jalankan DFS mulai dari node 'A'
print("DFS dari A:")
dfs(graph, 'A', visited)

#===============================================================
# Pertanyaan Analisis DFS:
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
# 2. Apa yang terjadi jika urutan neighbor diubah?
# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
#===============================================================
# Penjelasan & Jawaban:
# 1. DFS masuk ke node terdalam terlebih dahulu karena ia menggunakan struktur data stack
#    (baik secara eksplisit maupun melalui rekursi) yang memungkinkan untuk "menyimpan" jalur
#    yang sedang dieksplorasi. Ketika DFS menemukan sebuah node, ia akan terus mengeksplorasi
#    node tersebut dan anak-anaknya sebelum kembali ke node sebelumnya, sehingga memastikan
#    bahwa jalur terdalam dieksplorasi terlebih dahulu.
# 2. Jika urutan neighbor diubah, maka urutan kunjungan DFS juga akan berubah.
#    DFS akan mengikuti urutan neighbor yang diberikan, sehingga jika urutan tersebut
#    diubah, maka jalur yang dieksplorasi juga akan berbeda. Ini bisa menghasilkan hasil
#    yang berbeda dalam hal urutan node yang dikunjungi.
# 3. Hasil DFS dan BFS pada graph yang sama akan berbeda dalam hal urutan node yang dikunjungi.
#    DFS akan mengeksplorasi jalur terdalam terlebih dahulu, sementara BFS akan mengeksplorasi
#    semua node pada level yang sama sebelum melanjutkan ke level berikutnya. Oleh karena itu,
#    urutan kunjungan node dalam DFS dan BFS bisa sangat berbeda tergantung pada struktur graph
#    dan urutan neighbor yang diberikan.
#===============================================================