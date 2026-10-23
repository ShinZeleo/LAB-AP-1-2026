def format_set(himpunan):
    """Menampilkan set dengan urutan alfabet agar output selalu konsisten."""
    return "{" + ", ".join(repr(item) for item in sorted(himpunan)) + "}"


def daftar_kandidat(kandidat_set, nama):
    """Mendaftarkan kandidat ke dalam set (nama otomatis di-capitalize)."""
    nama = nama.strip().capitalize()

    if nama in kandidat_set:
        print(f"Error! '{nama}' sudah terdaftar sebagai kandidat.")
        return False

    kandidat_set.add(nama)
    print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")
    return True


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    """Mencatat suara pemilih ke dalam dictionary {nama_pemilih: kandidat}."""
    pemilih = nama_pemilih.strip().lower()
    pilihan = pilihan.strip().capitalize()
    tampil_pemilih = pemilih.capitalize()

    if pilihan not in kandidat_set:
        print(f"Error! Kandidat '{pilihan}' tidak ada dalam daftar. "
              f"Suara tidak dicatat.")
        return False

    if pemilih in rekap_suara:
        print(f"'{tampil_pemilih}' sudah memberikan suara sebelumnya!")
        return False

    rekap_suara[pemilih] = pilihan
    print(f"Suara '{tampil_pemilih}' untuk '{pilihan}' berhasil dicatat!")
    return True


def hitung_suara(rekap_suara, kandidat_set):
    """Menghitung perolehan suara tiap kandidat (kandidat tanpa suara = 0)."""
    perolehan = {kandidat: 0 for kandidat in kandidat_set}
    for kandidat_dipilih in rekap_suara.values():
        perolehan[kandidat_dipilih] += 1
    return perolehan


def tampilkan_hasil(perolehan):
    """Menampilkan hasil pemilihan, total suara, dan pemenang/seri."""
    garis = "=" * 40
    print(garis)
    print("  HASIL PEMILIHAN KETUA KELAS")
    print(garis)

    for kandidat in sorted(perolehan):
        print(f"  {kandidat}: {perolehan[kandidat]} suara")

    total = sum(perolehan.values())
    print()
    print(f"Total suara masuk: {total}")

    if total == 0:
        print("Belum ada suara yang masuk.")
    else:
        tertinggi = max(perolehan.values())
        pemenang = sorted(k for k, v in perolehan.items() if v == tertinggi)

        if len(pemenang) > 1:
            print(f"Hasil SERI antara: {', '.join(pemenang)}")
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")

    print(garis)


def main():
    kandidat_set = set()
    rekap_suara = {}
    garis = "=" * 40

    print(garis)
    print("  SISTEM PEMILIHAN KETUA KELAS")
    print(garis)

    # ----- Fase Pendaftaran -----
    print()
    print("--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()

        if nama == "":
            if len(kandidat_set) < 2:
                print("Minimal harus ada 2 kandidat sebelum bisa lanjut!")
                continue
            break

        daftar_kandidat(kandidat_set, nama)

    print()
    print(f"Kandidat terdaftar: {format_set(kandidat_set)}")

    # ----- Fase Pemungutan Suara -----
    print()
    print("--- FASE PEMUNGUTAN SUARA ---")
    while True:
        print()
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
        if nama_pemilih == "":
            break

        print(f"Kandidat yang tersedia: {format_set(kandidat_set)}")
        pilihan = input("Pilih kandidat: ")
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

    # ----- Hasil -----
    print()
    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)


if __name__ == "__main__":
    main()