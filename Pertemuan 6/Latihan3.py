#===============================================================
# Nama   : Mayta Nabila Syahira
# NIM    : J0403251065
# Kelas  : P/B2
#===============================================================

#===============================================================
# Latihan 3 : Tracing Insertion Sort (Analysis)
#===============================================================

def insertion_sort_tracing(data):
    # Output awal untuk mempermudah pemahaman proses
    print(f"Data Awal: {data}")
    print("-" * 40)
    
    # Perulangan dimulai dari elemen ke-2 (index 1) hingga akhir
    for i in range(1, len(data)):
        key = data[i]  # Angka yang sedang "diambil" untuk dicarikan posisi
        j = i - 1      # Memulai perbandingan dari elemen sebelah kiri key
        
        # Proses pergeseran (Shifting)
        # Selama angka di kiri lebih besar dari key, geser ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        
        # Menyisipkan key ke posisi yang sudah kosong/benar
        data[j + 1] = key
        
        # Menampilkan status list setelah setiap putaran i selesai
        print(f"Iterasi i = {i} (key={key}): {data}")

# Data input dari soal
data_tugas = [5, 2, 4, 6, 1, 3]
insertion_sort_tracing(data_tugas)

'''
Soal:
1. Tuliskan isi list setelah iterasi i = 1.
2. Tuliskan isi list setelah iterasi i = 3.
3. Berapa kali pergeseran terjadi pada iterasi i = 4?

Jawaban:
1. Isi list i = 1: [2, 5, 4, 6, 1, 3] karena key = 2 lebih kecil dari 5 sehingga 5 geser ke kanan dan 2 masuk ke depan.
2. Isi list i = 3: [2, 4, 5, 6, 1, 3] karena key = 6 sudah lebih besar dari angka 5 di kirinya, jadi tidak ada angka yang geser.
3. Pergeseran i = 4: Terjadi 4 kali geser karena key = 1 lebih kecil dari semua angka di kirinya (6, 5, 4, 2) sehingga semuanya harus geser.
'''