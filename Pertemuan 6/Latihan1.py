#===============================================================
# Nama   : Mayta Nabila Syahira
# NIM    : J0403251065
# Kelas  : P/B2
#===============================================================

#===============================================================
# Latihan 1 : Memahami Kode Program (Insertion Sort)
#===============================================================
def insertion_sort(data):
    # Gambaran jawaban no 1, perulangan dari index 1 karena elemen ke-0 
    for i in range(1, len(data)):
        # Gambaran jawaban no 2, variabel 'key' menyimpan sementara nilai yang 
        # akan disisipkan agar tidak hilang saat proses pergeseran.
        key = data[i]
        key = data[i]
        j = i - 1
        
        # Gambaran jawaban no 3&4
        # Proses mencari posisi dan menggeser angka yang lebih besar
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            
        # Menyisipkan key ke tempat yang benar
        data[j + 1] = key
        
    return data # Harus sejajar dengan FOR, bukan di dalam FOR

'''
Soal:
1. Mengapa perulangan dimulai dari indeks 1?
2. Apa fungsi variabel key?
3. Mengapa digunakan while, bukan for?
4. Operasi apa yang terjadi di dalam while?

Jawaban:
1. Karena elemen pertama (index 0) dianggap sudah rapi sebagai patokan di awal, jadi mulai ambil data dari elemen kedua
2. Sebagai tempat menyimpan sementara angka yang mau dipindah, supaya tidak hilang saat angka lain digeser.
3. Karena kita nggak tahu harus mundur berapa kali. (while) bakal berhenti otomatis begitu ketemu angka yang lebih kecil atau sudsah mentok di ujung kiri
4. Operasi pergeseran (shifting) angka yang lebih besar ke arah kanan untuk memberi ruang buat si (key).
'''