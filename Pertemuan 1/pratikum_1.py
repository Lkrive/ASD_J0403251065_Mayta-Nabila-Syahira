# ==========================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 1A: Membaca seluruh isi file
# ==========================================================

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() # Membaca seluruh isi file sebagai string
# Menampilkan isi file ke layar
print("=== Isi File Data Mahasiswa ===")
print(isi_file)

# ==========================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 1B: Membaca file per baris
# ==========================================================
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() # Menghapus karakter newline
print(baris)

# ==========================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 1C: Analisis read() vs baca per baris
# ==========================================================
# -------------------------------
# Bagian A: Baca file dengan read()
# -------------------------------
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() # seluruh isi file jadi 1 string besar
print("=== HASIL READ() ===")
print("Tipe data:", type(isi_file))
print("Jumlah karakter:", len(isi_file))
print("Jumlah baris:", isi_file.count("\n") + 1)

# -------------------------------
# Bagian B: Baca file per baris
# -------------------------------
jumlah_baris = 0
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
print("Baris ke-", jumlah_baris)
print("Isinya :", baris)

#================================================
# Pratikum 1 : Konsep ADT dan File Handling
# LAtihan dasar 3: Parsing menjadi kolom data
#================================================

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print("NIM: ", nim, "| Nama: ", nama, "| Nilai: ", nilai)

#====================================================
# Pratikum 1 : Konsep ADT dan file Handling
# LAtihan dasar 3: Membaca file dan Menyimpan ke list
#====================================================

data_list = [] # List untuk menampung data mahasiswa

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        # Simpan sebagai list "[nim, nama, nilai]"
        data_list.append([nim, nama, int(nilai)])

print("====Data Mahasiswa dalam List====")
print(data_list)

print("====Jumlah record dalama List====")
print("Jumlah record:", len(data_list))

print("====Menampilkan data record tertentu====")
print("Contoh record pertama: ", data_list[0])

#============================================================
# Pratikum 1 : Konsep ADT dan File Handling
# LAtihan dasar 4: Membaca file dan Menyimpan file dictionary
#============================================================

data_dict={} # buat variabel untuk dictionary
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #Simpan data mahasiswa ke dictionary dengan key NTM
        data_dict[nim] = {          #key
            "nama": nama,           #values
            "nilai": int(nilai)     #values
        }
print("====Data Mahasiswa dalam Dictionary==")
print(data_dict)