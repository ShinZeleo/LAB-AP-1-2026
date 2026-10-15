def format_set(kumpulan):
    return '{' + ', '.join(repr(item)for item in sorted(kumpulan)) + '}'

def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()
    if nama in kandidat_set:
        print(f'"{nama}" sudah terdaftar sebelumnya!')
        return False
    kandidat_set.add(nama)
    print(f'"{nama}" berhasil didaftarkan sebagai kandidat!')
    return True

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_tampil = nama_pemilih.strip().capitalize()
    kunci_pemilih = nama_tampil.lower()
    pilihan = pilihan.strip().capitalize()

    if pilihan not in kandidat_set:
        print(f'Error: Kandidat "{pilihan}" tidak terdaftar! Suara tidak dicatat.')
        return False
    if kunci_pemilih in rekap_suara:
        print(f'"{nama_tampil}" sudah memberikan suara sebelumnya!')
        return False

    rekap_suara[kunci_pemilih] = pilihan
    print(f'Suara "{nama_tampil}" untuk "{pilihan}" berhasil dicatat!')
    return True

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in sorted(kandidat_set):
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan

def tampilkan_hasil(perolehan):
    print("="*40)
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("="*40)
    for kandidat, jumlah in perolehan.items():
        print(f'{kandidat}: {jumlah} suara')

    total_suara = sum(perolehan.values())
    print(f'\nTotal suara masuk: {total_suara}')

    if total_suara == 0:
        print('Belum ada suara yang masuk.')
        print('Perlu dilakukan pemilhan ulang')
    else:
        tertinggi = max(perolehan.values())
        pemenang = [k for k, v in perolehan.items() if v == tertinggi]

        if len(pemenang) == 1:
            print(f'PEMENANG: {pemenang[0]} dengan {tertinggi} suara!')
        else:
            print(f'Hasil SERI antara: {', '.join(pemenang)}')
            print('Perlu dilakukan pemilhan ulang!')
        print("="*40)

kandidat_set = set()
rekap_suara = {}

print("="*40)
print(" SISTEM PEMILIHAN KETUA KELAS")
print("="*40)

print('\n--- FASE PENFDAFTARAN KANDIDAT ---')
while True:
    nama = input('Masukkan nama kandidat (kosongkan untuk selesai):').strip()
    if nama == "":
        if len(kandidat_set) < 2:
            print(f'Minimal harus ada 2 kandidat! Saat ini baru ada {len(kandidat_set)}.')
            continue
        break
    daftar_kandidat(kandidat_set, nama)

print(f'\nKandidat terdaftar: {format_set(kandidat_set)}')

print(f'\n--- FASE PEMUNGUTAN SUARA ---')
while True:
    print()
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
    if nama_pemilih == "":
        break
    print(f'Kandidat yang tersedia: {format_set(kandidat_set)}')
    pilihan = input("Pilih kandidat: ")
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

print()
perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)