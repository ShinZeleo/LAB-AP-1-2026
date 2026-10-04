def hitung_statistik (*nilai):
    rata = sum(nilai) / len(nilai)
    return rata,max(nilai),min(nilai)

def ke_angka(nilai):
    try:
        return int(nilai)
    except ValueError:
        return float(nilai)
daftar = []
while True:
    nilai = input("masukkan nilai ujian siswa (kososngkan untuk selesai): ")
    if nilai == "":
        break
    daftar.append(ke_angka(nilai))

if len(daftar) == 0:
    print("data nilai tidak tersedia.")
else: 
    rata, tertinggi, terendah = hitung_statistik(*daftar)
    print(f"rata-rata kelas: {rata}")
    print(f"nilai tertinggi: {tertinggi}")
    print(f"nilai terendah:  {terendah}")
