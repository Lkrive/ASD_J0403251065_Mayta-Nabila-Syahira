#===============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#===============================================================

#===============================================================
# Materi 2 : Insertion Sort (Tracing)
#===============================================================

def insertion_sort(data):
    #Melihat data awal
    print("data awal: ", data)
    print("="*50)
        
    #Loop mulai dari data ke 2 (index array ke 1)
    for i in range (1, len(data)):


        key = data[i] # simpan nilai yang disiispkan
        j = i-1 #index elemen terakhir di bagian kiri
        print("Iterasi ke- ", i)
        print("Nilai key = ", key)
        print("Bagian kiri(terurut): ", data[:i])
        print("Bagian Kanan(belum terurut): ", data[i:])

        #Geser
        while j>=0 and data[j]>key:
            data [j+1] = data[j]
            j -= 1

        #Sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disispkan : ", data)
        print("-"*50)
    return data
    
angka = [7,8,5,2,4,6]
print("Hasil Sorting: ", insertion_sort(angka))