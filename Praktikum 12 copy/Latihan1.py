#===============================================================
# Nama    : Mayta Nabila Syahira
# NIM     : J0403251065
# Kelas   : P/B2
#===============================================================

#===============================================================
# Latihan 1 : Weighted Graph dan Perhitungan Jalur
#===============================================================

# Representasi weighted graph menggunakan dictionary bersarang 
graph = { 
    'A': {'B': 4, 'C': 2}, # A terhubung ke B dengan bobot 4, dan ke C dengan bobot 2
    'B': {'D': 5},         # B terhubung ke D dengan bobot 5
    'C': {'D': 1},         # C terhubung ke D dengan bobot 1
    'D': {} 
} 
 
# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D']   # A -> B -> D  
jalur_2 = graph['A']['C'] + graph['C']['D']   # A -> C -> D 
 
print("Jalur 1: A -> B -> D =", jalur_1)  # Output: Jalur 1: A -> B -> D = 9
print("Jalur 2: A -> C -> D =", jalur_2)  # Output: Jalur 2: A -> C -> D = 3

if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D")
    
# Pertanyaan Analisis:
# 1. Berapa total bobot jalur A -> B -> D?
# 2. Berapa total bobot jalur A -> C -> D?
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?

# Penjelasan & Jawaban:
# 1. Total bobot jalur A -> B -> D adalah 4 (A ke B) + 5 (B ke D) = 9.
#    Jadi kalau lewat B, total jaraknya lumayan besar.
# 2. Total bobot jalur A -> C -> D adalah 2 (A ke C) + 1 (C ke D) = 3.
#    Jalur ini lebih kecil karena bobotnya lebih ringan.
# 3. Jalur yang dipilih sebagai jalur terpendek adalah A -> C -> D,
#    karena total bobotnya paling kecil dibanding jalur lainnya.
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge paling sedikit
#    karena yang dihitung itu total bobot, bukan jumlah langkah.
#    Bisa aja jalurnya lebih panjang (lebih banyak edge),
#    tapi karena bobot tiap edge kecil, hasil akhirnya tetap lebih cepat.
#    Jadi yang penting itu total bobotnya, bukan banyaknya edge.


# tambahkan komentar sesuai bahasa kalian sendiri atau pemahaman kalian sendiri untuk menjelaskan setiap bagian kode yang ada
# pakai distraksi untk latihan ke-5