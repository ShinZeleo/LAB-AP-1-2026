#Input
jumlah = int(input("Masukkan jumlah mahasiswa: "))
hadir = 0
izin = 0
sakit = 0
alpa = 0
mahasiswa = 1

#Perhitungan absen
while mahasiswa <= jumlah:
    status = input (f"Mahasiswa ke-{mahasiswa}: ")
    if status =="H":
        hadir += 1
        mahasiswa += 1
    elif status =="I":
        izin +=1
        mahasiswa +=1
    elif status =="S":
        sakit +=1
        mahasiswa +=1
    elif status =="A":
        alpa +=1
        mahasiswa +=1
    else:
        print("Status tidak valid")
        continue

print()
print("Hadir:", hadir)
print("Izin:", izin)
print("sakit:", sakit)
print("Alpa:", alpa)