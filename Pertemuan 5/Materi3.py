#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

#============================================================
# Materi 3 Rekursif : Menjumlahkan Elemen List
#============================================================

def jumlah_list(data, index=0):
    #basecase
    if index == len(data):
        return 0
    
    #recursive case
    return data[index] + jumlah_list(data, index+1)

print("=====Program Jumlah data=====")
print(jumlah_list([2, 4, 5]))