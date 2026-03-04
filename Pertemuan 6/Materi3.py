#===============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#===============================================================

#===============================================================
# Materi 3 : Insertion Sort (Merge Sort-Ascending1)
#===============================================================
#===============================================================
# Nama   : Mayta Nabila Syahira
# NIM    : J0403251065
# Kelas  : P/B2
#===============================================================

#===============================================================
# Materi 3 : Merge Sort (Ascending)
#===============================================================

def merge_sort(data):
    # Base Case: Kalau data cuma 1 atau kosong, ya udah pasti urut
    if len(data) <= 1:
        return data
    
    # Divide: Belah data jadi dua bagian (kiri & kanan)
    mid = len(data) // 2
    left = data[:mid] 
    right = data[mid:] 
    
    # Recursive Call: Belah terus sampai sisa 1 elemen
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Conquer: Gabungin lagi sambil diurutin
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = 0 # Indeks buat tim kiri
    j = 0 # Indeks buat tim kanan

    # Membandingkan elemen kiri dan kanan satu per satu
    while i < len(left) and j < len(right):
        # --- PERBAIKAN DI SINI ---
        if left[i] <= right[j]: # Cek, mana yang lebih kecil?
            result.append(left[i]) # Kalau kiri kecil, masukin kiri
            i += 1
        else:
            result.append(right[j]) # Kalau kanan kecil, masukin kanan
            j += 1
            
    # Menambahkan sisa elemen (kalau ada tim yang masih sisa anggotanya)
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Data uji
angka = [13, 7, 28, 5, 19, 26, 4]
print("===== Program Merge Sort =====")
print("Data Awal    :", angka)
print("Hasil Sorting:", merge_sort(angka))