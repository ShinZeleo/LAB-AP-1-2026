nilai_tes = int(input("Masukkan Nilai Tes: "))

if nilai_tes >= 80:
    print ("Lolos ke Tahap Wawancara")
elif nilai_tes >= 65:
    pengalaman_kerja = int(input("Masukkan Pengalaman Kerja (Tahun): "))
    if pengalaman_kerja >= 2:
        print ("Lolos Bersyarat")
else:
    print ("Tidak Lolos")