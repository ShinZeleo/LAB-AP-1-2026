def hitung_statistik(*nilai):
    """Menerima nilai dalam jumlah bebas, mengembalikan (rata-rata, tertinggi, terendah)"""
    rata_rata = sum(nilai) / len(nilai)
    return rata_rata, max(nilai), min(nilai)

def ubah_ke_angka(teks):
    """Ubah teks ke int jika bisa, jika tidak ke float"""
    try:
        return int(teks)
    except ValueError:
        return float(teks)

def main():
    daftar_nilai = []

    while True:
        masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ").strip()
        if masukan == "":
            break
        daftar_nilai.append(ubah_ke_angka(masukan))

    if len(daftar_nilai) == 0:
        print("Data nilai tidak tersedia.")
    else:
        rata_rata, tertinggi, terendah = hitung_statistik(*daftar_nilai)
        print(f"Rata-rata kelas: {rata_rata}")
        print(f"Nilai tertinggi: {tertinggi}")
        print(f"Nilai terendah: {terendah}")

main()