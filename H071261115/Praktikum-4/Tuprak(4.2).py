def statistik_nilai(*args):
    if len(args) == 0:
        return None
    rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah = min(args)
    return rata, tertinggi, terendah
 
 
nilai_list = []
 
while True:
    nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if nilai == "":
        break
    try:
        angka = int(nilai)
    except ValueError:
        angka = float(nilai)
    nilai_list.append(angka)
 
hasil = statistik_nilai(*nilai_list)
 
if hasil is None:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = hasil
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
 