def hitung_statistik(*nilai):
    if len(nilai) == 0:
        return None
    rata_rata = sum(nilai)/len(nilai)
    return rata_rata, max(nilai), min(nilai)

daftar_nilai = []
def ubah_ke_angka(input_nilai):
    try:
        return int(input_nilai)
    except ValueError:
        return float(input_nilai)
    
while True:
    input_nilai = input('Masukkan nilai ujian siswa (kosongkan untuk selesai): ')
    if input_nilai == "" :
        break
    daftar_nilai.append(ubah_ke_angka(input_nilai))
    
hasil = hitung_statistik(*daftar_nilai)
 
if hasil is None:
    print("Data nilai tidak tersedia.")

else:
    rata_rata, tertinggi, terendah = hasil
    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
