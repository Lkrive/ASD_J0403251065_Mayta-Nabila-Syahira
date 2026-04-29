#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Materi 3 : Implementasi DFS (Depth-First Search) pada Graph
#===============================================================

#representasi graph menggunakan adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': [],
    'G': []

}

def dfs(graph, node, visited):
#Fungsi untuk melakukan penelusuran graph dengan metode DFS
# graph : dictionary yang menyimpan struktur dari graph
# node : meninmpa node yang sedang dikunjungi 
#visited : menyimpan node yang sudah dikunjungi

#tandai node ini sebagai node yang sudah dikunjungi
 visited.add(node)

#tampilkan node yang sedang dikunjungi
 print(node, end=' ')

#periksa semua tetangga dari node saat ini
 for neighbor in graph[node]: #iterasi untuk setiap tetangga dari node

    #jika tetangga belum pernah dikunjungi 
    if neighbor not in visited:
        #melakukan dfs secara rekursif ke tetangga tersebut
        dfs(graph, neighbor, visited) 

# Set kosong untuk menyimpan node yang sudah dikunjungi 
visited = set() 

#Menjalankan dfs dari node A 
print("Urutan DFS:") 
dfs(graph, 'A', visited) 