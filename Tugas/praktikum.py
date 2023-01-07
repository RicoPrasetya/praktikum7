print("Nama : Rico Prasetya")
print("NIM  : 312210425")

data = {}
while True :
    print("")
    j = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ")
# untuk Keluar Dari Program
    if j.lower() == "k":
        print("Keluar Dari Program")
        break
# untuk melihat-lihat
    elif j.lower() == "l":
        if data.items():
            print("Daftar Nilai")
            print()
            print("=============================================================================================");
            print("|  No  |    Nama    |      NIM      |    Tugas    |     UTS     |     UAS     | Nilai Akhir |");
            print("=============================================================================================");
            i = 0
            for x in data.items():
                i+=i
                print("|  1   | {0:9}  |   {1:9}   |  {2:9}  |  {3:9}  |  {4:9}  |  {5:9}  |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
                print("=============================================================================================");
                print("")
        else :
            print("Daftar Nilai")
            print()
            print("=============================================================================================");
            print("|  No  |    Nama    |      NIM      |    Tugas    |     UTS     |     UAS     | Nilai Akhir |");
            print("=============================================================================================");
            print("|                                      TIDAK ADA DATA                                       |");
            print("=============================================================================================");
# Untuk Menambahkan Data
    elif j.lower() == "t":
        print("Tambah Data")
        nama  = input    ("Nama       : ")
        nim   = input    ("NIM        : ")
        tugas = int(input("Nilai Tugas: "))
        uts   = int(input("Nilai UTS  : "))
        uas   = int(input("Nilai UAS  : "))
        nilaiakhir = ((tugas)*30/100+(uts)*35/100+(uas)*35/100)
        data[nama] = [nim, tugas, uts, uas, nilaiakhir]
# Untuk Mengubah data
    elif j.lower() == "u":
        print("Edit Data Nilai Mahasiswa")
        nama  = input    ("Nama       : ")
        if nama in data.keys():
            nim   = input    ("NIM        : ")
            tugas = int(input("Nilai Tugas: "))
            uts   = int(input("Nilai UTS  : "))
            uas   = int(input("Nilai UAS  : "))
            nilaiakhir = ((tugas)*30/100+(uts)*35/100+(uas)*35/100)
            data[nama] = [nim, tugas, uts, uas, nilaiakhir]
        else:
            print("Data nilai{0} tidak ada".format(nama))
# Untuk Menghapus Data
    elif j.lower() == "h":
        print("Hapus Data Nilai Mahasiswa")
        nama  = input    ("Nama       : ")
        if nama in data.keys():
            del data[nama]
        else:
            print("Data {0} tidak ada".format(nama))
# Untuk Mencari Data
    elif j.lower() == "c":
        print("Cari Data Nilai Mahasiswa")
        nama  = input    ("Nama       : ")
        if nama in data.keys():
            print("")
            print("=====================================================================================");
            print("|   {0}   |   {1}   |".format(nama, data[nama]))
            print("=====================================================================================");
        else:
            print("Datanya {0} tidak ada".format(nama))
    else:
        print()
        print("=====================================================================================");
        print("|  No  |     Nama     |     NIM     |   Tugas   |   UTS   |   UAS   |  Nilai Akhir  |");
        print("=====================================================================================");
        print("|                                   TIDAK ADA DATA                                   ");
        print("=====================================================================================");
else:
    print("Pilih Menu Yang Tersedia")