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
1. Isi list setelah iterasi i = 1 adalah [2, 5, 4, 6, 1, 3].
   Penjelasan: i=1 berarti key adalah 2. Karena 5 > 2, angka 5 digeser ke kanan 
   dan 2 disisipkan di posisi awal (index 0).
2. Isi list setelah iterasi i = 3 adalah [2, 4, 5, 6, 1, 3].
   Penjelasan: Pada i=2, key adalah 4 (hasilnya [2, 4, 5, ...]). Pada i=3, 
   key adalah 6. Karena 5 < 6, tidak ada pergeseran yang terjadi, sehingga 
   urutan tetap [2, 4, 5, 6, 1, 3].
3. Pada iterasi i = 4, terjadi sebanyak 4 kali pergeseran.
   Penjelasan: Pada i=4, key adalah 1. Program membandingkan 1 dengan [2, 4, 5, 6]. 
   Karena semua angka tersebut lebih besar dari 1, maka terjadi 4 kali operasi 
   geser: angka 6 geser, 5 geser, 4 geser, dan 2 geser, untuk memberi ruang 
   bagi angka 1 di posisi paling depan.
'''