
#===============================================================
# Nama   : Mayta Nabila Syahira
# NIM    : J0403251065
# Kelas  : P/B2
#===============================================================

# ==========================================================
# Latihan 5 : Melengkapi Fungsi Merge
# ==========================================================

def merge(left, right):
    result = []
    i = 0
    j = 0

    # Membandingkan elemen dari list kiri dan kanan
    while i < len(left) and j < len(right):
        # Jawaban No 1: Kondisi Ascending
        if left[i] <= right[j]: 
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Menambahkan sisa elemen yang belum dimasukkan
    result.extend(left[i:])
    result.extend(right[j:])

    return result

'''
Soal:
1. Lengkapi kondisi agar menjadi ascending.
2. Jelaskan fungsi result.extend().

Jawaban :
1. Kondisi agar ascending adalah if left[i] <= right[j]. Dengan kondisi ini, 
   program akan memilih nilai yang lebih kecil untuk dimasukkan terlebih dahulu 
   ke dalam list hasil.
2. Fungsi result.extend() digunakan untuk mengambil semua sisa elemen yang 
   masih ada di list left atau right dan menambahkannya ke akhir list result. 
   Ini penting karena biasanya ada salah satu list yang habis lebih dulu.
'''