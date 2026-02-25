#============================================================
# Nama  : Mayta Nabila Syahira
# NIM   : J0403251065
# Kelas : P/B2
#============================================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum pada List (Rekursif)
# ==========================================================

def cari_maks(data, index=0):
    # 1. BASE CASE (Kondisi Berhenti)
    # Jika index sudah mencapai elemen terakhir dalam list,
    # maka nilai tersebut dianggap sebagai nilai maksimum sementara 
    # untuk dibandingkan dengan elemen sebelumnya.
    if index == len(data) - 1:
        return data[index]
    
    # 2. RECURSIVE CALL (Pemanggilan Diri Sendiri)
    # Fungsi memanggil dirinya sendiri untuk mengecek elemen di index selanjutnya.
    # Program akan terus memanggil hingga mencapai ujung list (Base Case).
    maks_sisa = cari_maks(data, index + 1)
    
    # 3. LOGIKA PERBANDINGAN (Backtracking)
    # Setelah mencapai ujung, program akan membandingkan elemen saat ini 
    # dengan nilai maksimum yang didapat dari elemen-elemen setelahnya.
    if data[index] > maks_sisa:
        return data[index] # Jika elemen sekarang lebih besar, kembalikan elemen ini
    else:
        return maks_sisa    # Jika tidak, teruskan nilai maksimum yang sudah ada

# Data uji
angka = [3, 7, 2, 9, 5]
print("===== Program Mencari Nilai Maksimum =====")
print("Data List:", angka)
print("Nilai maksimum:", cari_maks(angka))