#Tugas no 3
nilai_tes = int(input("Masukkan nilai tes: "))
pengelaman_kerja = int(input("Masukkan pengalaman kerja (tahun): "))

if nilai_tes >=80:
    print ("Lolos ke Tahap Wawancara")
elif nilai_tes >=65 and pengelaman_kerja >=2:
    print ("Lolos Bersyarat")
else:
    print("Tidak Lolos")