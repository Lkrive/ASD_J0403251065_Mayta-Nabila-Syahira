#===============================================================
# Nama   : Mayta Nabila Syahira
# NIM    : J0403251065
# Kelas  : P/B2
#===============================================================

#===============================================================
# Latihan 2 : Melengkapi Potongan Kode
#===============================================================
def insertion_sort(data, tipe="ascending"):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        # gambaran jawaban no 1&2
        if tipe == "ascending":
            # Selama angka di kiri LEBIH BESAR, geser ke kanan
            while j >= 0 and data[j] > key: 
                data[j + 1] = data[j]
                j -= 1
        else:
            # selama angka di kiri LEBIH KECIL, maka geser ke kanan (Descending)
            while j >= 0 and data[j] < key:
                data[j + 1] = data[j]
                j -= 1
            
        # titik-titik terakhir diisi dengan penempatan key
        data[j + 1] = key 
        
    return data

# Uji Coba
angka = [13, 7, 28, 5]
print("Ascending  :", insertion_sort(angka.copy(), "ascending"))
print("Descending : ", insertion_sort(angka.copy(), "descending"))
    
'''
Soal:
1. Lengkapi kondisi agar menjadi sorting ascending(Kecil ke Gede).
2. Ubah agar menjadi descending.

Jawaban:
1. Isi dengan data[j]> key #karena kita mau geser angka kanan yang JIKA angka di sebelah kirinya (data[j]) > dari angka yang dipegang (key)
2. Isi dengan data[j]< key #karena di sini kita mau geser angka ke kanan kalau angka di kiri itu lebih kecil. Jadi angka yang paling gede bakal "nendang" angka kecil ke belakang

'''