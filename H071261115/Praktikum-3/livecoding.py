# Input jumlah mahasiswa (validasi angka dan harus > 0)
while True:
    try:
        jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    except ValueError:
        print("Jumlah mahasiswa harus berupa angka!")
        continue
 
    if jumlah_mahasiswa <= 0:
        print("Jumlah mahasiswa harus lebih dari 0!")
        continue
 
    break
 
print()
 
total_nilai = 0
jumlah_valid = 0  # menghitung berapa nilai yang benar-benar terpakai
 
mahasiswa_ke = 1
while mahasiswa_ke <= jumlah_mahasiswa:
    try:
        nilai = int(input(f"Nilai mahasiswa ke-{mahasiswa_ke}: "))
    except ValueError:
        print("Nilai harus berupa angka!")
        continue
 
    if nilai < 0 or nilai > 100:
        print("Nilai tidak valid!")
        continue
 
    total_nilai += nilai
    jumlah_valid += 1
    mahasiswa_ke += 1
 
rata_rata = total_nilai / jumlah_valid
 
print()
print(f"Total nilai: {total_nilai}")
print(f"Rata-rata: {rata_rata}")
 