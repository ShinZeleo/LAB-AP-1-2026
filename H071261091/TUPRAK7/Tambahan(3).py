def simpan_nilai(nama, nilai):
    try:
        with open("nilai.txt", "a") as file:
            file.write(f"{nama}, {nilai}\n")
    except IOError:
        print("Error: Gagal menyimpan data.")

def tampilkan_nilai():
    try:
        with open("nilai.txt", "r") as file:
            print("\nDaftar Nilai Mahasiswa:")
            print (file.read())           
    except IOError:
        print("Error: Gagal membaca data.")

while True:
    nama = input ("Nama Mahasiswa(Kosongkan untuk selesai): ")
    if nama == "":
        break
    nilai = int(input("Nilai Mahasiswa: "))
    print ("Data berhasil disimpan.\n")
    simpan_nilai(nama, nilai)

tampilkan_nilai()