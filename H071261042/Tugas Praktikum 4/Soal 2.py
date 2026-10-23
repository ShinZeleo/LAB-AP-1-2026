#Output
def rekap_nilai(*args):
    rata_rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah = min(args)
    return rata_rata, tertinggi, terendah

#Processing program (Input)
def main():
    daftar_nilai = []
    while True:
        masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
        if masukan == "":
            break #Menghentikan proses input

        nilai = float(masukan)
        if nilai == int(nilai):
            nilai = int(nilai)
        daftar_nilai.append(nilai) 
    if len(daftar_nilai) == 0:
        print("Data nilai tidak tersedia.")
    else:
        rata_rata, tertinggi, terendah = rekap_nilai(*daftar_nilai)
        print(f"Rata-rata kelas: {rata_rata}")
        print(f"Nilai tertinggi: {tertinggi}")
        print(f"Nilai terendah: {terendah}")

main()