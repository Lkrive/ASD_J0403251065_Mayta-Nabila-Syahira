#============================================
# Pratikum 1 : Konsep ADT dan File Handling
# LAtihan dasar 1A: Membaca seluruh isi file
#============================================

# Membuka file dengan mode read ("r")
import os
path = os.path.dirname(__file__)
with open(os.path.join(path, "data_mahasiswa.txt"), "r", encoding="utf-8") as file:
   isi_file = file.read()
print(isi_file)

print("Hasil Read")
print("Tipe Data", type(isi_file))
print("Jumlah Karakter", len(isi_file))
print("jumlah baris", isi_file.count("\n")+1)

#Membuka file per baris
print("===Membaca File per Baris===")
Jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        Jumlah_baris = Jumlah_baris + 1
        baris = baris.strip() # menghilangkan baris baru \n
        print("Baris ke-: ", Jumlah_baris)
        print("Isinya: ", baris)

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