# ==============================================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
# Materi  : Latihan 1 - Representasi Weighted Graph
# ==============================================================================

# Menggunakan Dictionary untuk menyimpan adjacency list
# Key: Node asal, Value: List of tuples (Node tujuan, bobot)
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('Z', 6)],
    'E': [('C', 10), ('D', 2), ('Z', 3)],
    'Z': [('D', 6), ('E', 3)]
}

def tampilkan_graph(g):
    print("Representasi Weighted Graph (Adjacency List):") # Menampilkan graph dengan format yang mudah dibaca
    for node in g: # Iterasi setiap node dalam graph
        for tetangga, bobot in g[node]:
            # Menampilkan hubungan antar node beserta biayanya/bobotnya
            print(f"{node} --({bobot})--> {tetangga}")

tampilkan_graph(graph)

# Penjelasan: Graph ini direpresentasikan dengan Adjacency List. 
# Setiap node menyimpan daftar tetangganya beserta bobot edge yang menghubungkannya.

# Pertanyaan Analisis:
# 1. Apa perbedaan graph awal dan spanning tree? 
# 2. Mengapa spanning tree tidak boleh memiliki cycle? 
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?

# Penjelasan & Jawaban:
# 1. Graph awal bisa memiliki banyak edge dan cycle, sedangkan spanning tree adalah subgraph
#    yang menghubungkan semua node tanpa cycle dan dengan jumlah edge minimum.
# 2. Spanning tree tidak boleh memiliki cycle karena tujuan utamanya adalah menghubungkan 
#    semua node dengan biaya minimum. Cycle akan menambah biaya tanpa menambah konektivitas.
# 3. Jumlah edge spanning tree selalu lebih sedikit karena hanya menghubungkan semua node 
#    dengan tepat (n-1 edge untuk n node), sedangkan graph awal bisa memiliki banyak edge yang tidak 
#    diperlukan untuk menghubungkan semua node.

