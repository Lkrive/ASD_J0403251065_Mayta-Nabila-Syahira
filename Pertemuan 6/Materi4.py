#===============================================================
# Nama   : Mayta Nabila Syahira
# NIM    : J0403251065
# Kelas  : P/B2
#===============================================================

#===============================================================
# Materi 4 : Merge Sort (Ascending with Tracing)
#===============================================================

# Kita tambah parameter 'depth' biar bisa bikin indentasi otomatis
def merge_sort(data, depth=0):
    indent = "  " * depth # Membuat spasi sesuai kedalaman rekursi
    print(f"{indent}--> Masuk merge_sort({data})")

    # Base Case: Kalau data cuma 1, langsung balik badan
    if len(data) <= 1:
        return data
    
    # Divide: Belah data jadi dua bagian
    mid = len(data) // 2
    left = data[:mid] 
    right = data[mid:] 

    print(f"{indent}    Divide: {left} dan {right}")
    
    # Recursive Call: Panggil lagi sambil nambah depth-nya
    left_sorted = merge_sort(left, depth + 1)
    right_sorted = merge_sort(right, depth + 1)
    
    # Conquer: Gabungin lagi
    merged = merge(left_sorted, right_sorted)
    print(f"{indent}    Merge: {left_sorted} + {right_sorted} => {merged}")

    return merged

def merge(left, right):
    result = []
    i = j = 0 

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Data uji
angka = [13, 7, 28, 5, 19, 26, 4]
print("===== Program Tracing Merge Sort =====")
hasil = merge_sort(angka)
print("\n===== HASIL AKHIR =====")
print("Data Awal    :", angka)
print("Hasil Sorting:", hasil)
