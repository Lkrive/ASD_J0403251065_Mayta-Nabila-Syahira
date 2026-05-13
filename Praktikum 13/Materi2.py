import heapq 
 
graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} # Graph berbobot dengan bobot positif
 
def prim(graph, start): 
 
    visited = set([start]) # Set untuk menyimpan node yang sudah dikunjungi
 
    edges = [] 
 
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) # Memasukkan edge awal ke dalam priority queue (min-heap)
 
    mst = [] 
    total_weight = 0 
 
    while edges: 
 
        weight, u, v = heapq.heappop(edges) # Ambil edge dengan bobot terkecil
 
        if v not in visited: 
 
            visited.add(v) # Tandai node tujuan sebagai visited
 
            mst.append((u, v, weight)) # Menambahkan edge ke MST
            total_weight += weight # Menambahkan bobot edge ke total
 
            for neighbor, w in graph[v].items(): 
 
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) # Tambahkan edge dari node yang baru dikunjungi ke heap
 
    return mst, total_weight 
 
 
mst, total = prim(graph, 'A') # Memulai Prim dari node A # Menjalankan Prim untuk mendapatkan MST dan total bobot
 
print("Minimum Spanning Tree:") 
 
for edge in mst: # Mencetak edge yang dipilih dalam MST # Mencetak edge yang dipilih dalam MST
    print(edge) 
 
print("Total bobot =", total) 
