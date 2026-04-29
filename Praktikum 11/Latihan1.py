#=============================================================== 
# Nama    : Mayta Nabila Syahira 
# NIM     : J0403251065 
# Kelas   : P/B2 
#=============================================================== 
 
#=============================================================== 
# Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi) 
#=============================================================== 

# Representasi graph sebagai adjacency list (dictionary)
# Setiap key adalah node, value-nya adalah list tetangga yang bisa dikunjungi
graph = {  
    'Rumah': ['Sekolah', 'Toko'],        # Rumah terhubung ke Sekolah dan Toko
    'Sekolah': ['Perpustakaan'],          # Sekolah terhubung ke Perpustakaan
    'Toko': ['Pasar'],                    # Toko terhubung ke Pasar
    'Perpustakaan': [],                   # Perpustakaan tidak punya tetangga (daun)
    'Pasar': []                           # Pasar tidak punya tetangga (daun)
}  

# Import deque dari collections untuk digunakan sebagai antrian (queue) BFS
# deque lebih efisien dari list biasa untuk operasi popleft()
from collections import deque  

def bfs(graph, start):      
    visited = set()             # Set untuk menyimpan node yang sudah dikunjungi (menghindari duplikasi)
    queue = deque([start])      # Antrian BFS dimulai dari node awal

    visited.add(start)          # Tandai node awal sebagai sudah dikunjungi

    while queue:                # Selama antrian tidak kosong, terus proses
        node = queue.popleft()          # Ambil node pertama dari antrian (FIFO)
        print(node, end=" ")            # Cetak node yang sedang dikunjungi

        for neighbor in graph[node]:    # Iterasi semua tetangga dari node saat ini
            if neighbor not in visited:         # Jika tetangga belum dikunjungi
                visited.add(neighbor)           # Tandai sebagai sudah dikunjungi
                queue.append(neighbor)          # Tambahkan ke antrian untuk diproses berikutnya

# Jalankan BFS mulai dari node 'Rumah'
print("BFS dari Rumah:")
bfs(graph, 'Rumah')

#=============================================================== 
# Pertanyaan Analisis BFS: 
# 1. Node mana yang dikunjungi pertama?   
# 2. Mengapa BFS cocok untuk mencari jalur terdekat?   
# 3. Apa perbedaan urutan BFS jika struktur graph diubah?  
#=============================================================== 
# Penjelasan & Jawaban: 
# 1. Node yang dikunjungi pertama adalah "Rumah" karena BFS 
#    dimulai dari node tersebut. 
# 2. BFS cocok untuk mencari jalur terdekat karena ia mengeksplorasi 
#    semua node pada level yang sama sebelum melanjutkan ke level berikutnya, 
#    sehingga memastikan bahwa jalur pertama yang ditemukan adalah jalur terdekat. 
# 3. Urutan BFS akan berubah jika struktur graph diubah karena BFS mengikuti
#    urutan pengeksplorasian node berdasarkan level. Jika ada perubahan pada hubungan 
#    antar node, maka urutan kunjungan juga akan berubah sesuai dengan struktur baru graph tersebut. 
#===============================================================