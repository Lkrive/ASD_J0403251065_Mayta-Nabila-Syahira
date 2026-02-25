#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

#============================================================
# Materi 2 Rekursif : Call Stack
# Stracing bilangan (masuk-keluar)
#input 3
# Masuk 1 - 2 - 3
# Keluar
#3-2-1 | 1-2-3
#============================================================

def hitung(n):
    #base case
    if n == 0:
        print("selesai")
        return
    
    print("Masuk: ", n)
    hitung(n-1) #recursive case
    print("Keluar", n)

print("=================Program Tracing==============")
hitung(5)