#PROCESSING PROGRAM
#Program Untuk Mendaftarkan Kandidat
def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()
    if nama in kandidat_set: #jika nama telah terdaftar
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
        return False
    kandidat_set.add(nama) #jika nama belum terdaftar
    print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")
    return True

#Program Untuk Memberikan Suara
def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih = nama_pemilih.strip().lower()
    kandidat = pilihan.strip().capitalize()

    if kandidat not in kandidat_set:
        print(f"Error: Kandidat '{kandidat}' tidak ada! Suara tidak dicatat.")
        return False
    if pemilih in rekap_suara:
        print(f"'{nama_pemilih.strip()}' sudah memberikan suara sebelumnya!")
        return False

    rekap_suara[pemilih] = kandidat
    print(f"Suara '{nama_pemilih.strip()}' untuk '{kandidat}' berhasil dicatat!")
    return True

#Program Untuk Menghitung Suara
def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in kandidat_set} #semua kandidat terhitung dimulai 0
    for kandidat in rekap_suara.values():
        perolehan[kandidat] += 1
    return perolehan

#INPUT DAN OUTPUT PROGRAM 2
#Program Untuk Menampilkan Hasil Pemilihan
def tampilkan_hasil(perolehan):
    print("=" * 40)
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)

    urutan = sorted(perolehan.items(), key=lambda item: (-item[1], item[0])) #menghitung dari suara terbanyak ke suara tersedikit
    for nama, jumlah in urutan:
        print(f" {nama}: {jumlah} suara")

    total = sum(perolehan.values())
    print(f"Total suara masuk: {total}")

    if total == 0:
        print("Belum ada suara yang masuk, pemenang tidak dapat ditentukan.")
    else:
        tertinggi = max(perolehan.values())
        pemenang = sorted(k for k, v in perolehan.items() if v == tertinggi) #k=kandidat dan v=jumlah suara
        if len(pemenang) > 1:
            print(f"Hasil SERI antara: {', '.join(pemenang)}") #join list pemenang
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")
    print("=" * 40)

#INPUT DAN OUTPUT PROGRAM 1
#Program Utama
def main():
    kandidat_set = set()
    rekap_suara = {}

    print("=" * 40)
    print(" SISTEM PEMILIHAN KETUA KELAS")
    print("=" * 40)

    print("--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
        if nama == "":
            if len(kandidat_set) < 2:
                print("Minimal harus ada 2 kandidat sebelum melanjutkan!")
                continue
            break
        daftar_kandidat(kandidat_set, nama)
    print(f"Kandidat terdaftar: {kandidat_set}")

    print("--- FASE PEMUNGUTAN SUARA ---")
    while True:
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
        if nama_pemilih == "":
            break
        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ")
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan) #program untuk memberikan suara

    perolehan = hitung_suara(rekap_suara, kandidat_set) #program untuk menghitung suara
    tampilkan_hasil(perolehan) #program untuk menampilkan hasil pemilihan

main()