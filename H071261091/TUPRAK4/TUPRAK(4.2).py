def rekap_nilai (*nilai):
    if len(nilai) == 0:
        print ("Data nilai tidak tersedia.")
        return None

    rata_rata = sum(nilai)/len(nilai)
    nilai_tertinggi = max(nilai)
    nilai_terendah = min(nilai)

    return rata_rata, nilai_tertinggi, nilai_terendah

daftar_nilai = []

while True:
    input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ").strip()

    if input_nilai == "":
        break

    nilai = float(input_nilai)
    daftar_nilai.append(nilai)

rata, tertinggi, terendah = rekap_nilai(*daftar_nilai)

if rata is None:
    print ("data nilai tidak tersedia.")
else:
    tertinggi_int = int(tertinggi) if tertinggi.is_integer() else tertinggi
    terendah_int = int(terendah) if terendah.is_integer() else terendah

    print (f"Rata-rata kelas: {rata}")
    print (f"Nilai tertinggi: {tertinggi_int}")
    print (f"Nilai terendah: {terendah_int}")