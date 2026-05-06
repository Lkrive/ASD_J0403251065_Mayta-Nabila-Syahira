#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Materi 2 : Bellman Ford
#===============================================================

def bellman_ford(graph, start): 
 
    # Inisialisasi jarak semua node = tak hingga (belum diketahui)
    distances = {node: float('inf') for node in graph} 
    
    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0 
 
    # Relaksasi dilakukan sebanyak (jumlah node - 1) kali
    # Tujuannya biar semua kemungkinan jalur diperiksa
    for _ in range(len(graph) - 1): 
 
        # Loop semua node
        for node in graph: 
 
            # Loop semua tetangga dari node tersebut
            for neighbor, weight in graph[node].items(): 
 
                # Cek apakah ada jalur lebih pendek lewat node ini
                if distances[node] + weight < distances[neighbor]: 
 
                    # Kalau iya → update jaraknya
                    distances[neighbor] = distances[node] + weight 
 
    # Return hasil jarak terpendek
    return distances