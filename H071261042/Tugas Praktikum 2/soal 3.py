nilai = int(input("Masukkan nilai tes: "))
pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))

if nilai >= 80:
    print ("lolos ke tahap wawancara")
elif nilai >= 65 and pengalaman >= 2:
    print("Lolos bersyarat")
else:
    print("Tidak lolos")
