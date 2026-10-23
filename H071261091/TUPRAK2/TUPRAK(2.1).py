persentase_cabai = int(input("Masukkan Persentase Cabai: "))

if persentase_cabai < 0:
    print ("Input Tidak Valid")
elif persentase_cabai <= 10:
    print ("Level Aman")
elif persentase_cabai <= 40:
    print ("Level Sedang")
elif persentase_cabai <= 70:
    print ("Level Pedas")
else:
    print ("Level Ekstrem")