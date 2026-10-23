# TASK III
nilai_tes = int(input("Masukkan nilai tes : "))

if nilai_tes >= 80:
    print("Lolos ke Tahap Wawancara")
elif nilai_tes > 0 and nilai_tes < 80:
    pengalaman_kerja = int(input("Masukkan pengalaman kerja (tahun): "))
    if nilai_tes > 65 and pengalaman_kerja >= 2 :
        print("Lolos Bersyarat")
    else:
        print("Tidak Lolos")
else:
    print("Ulangi program")