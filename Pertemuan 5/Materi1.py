#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

#============================================================
# Materi 1 Rekursif : Faktorial
#  3! = 3 x 2 x 1 
# Base Case => 0 (Berhenti, hingga fungsi tidak jalan terus menerus)
# Recucrsive Case (Pemanggilan fungsinya sndiri dgn ukuran yang 
# dikurangi)
#============================================================

def faktorial(n):
    if n == 0:
        return 1
    #recursive case
    return n*faktorial(n-1) #n-*n-2*n-3*n-..... n-?
print("=========Program Faktorial==========")
print ("Hasil Faktorial : ", faktorial(3))
