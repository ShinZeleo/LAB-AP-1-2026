def tambah_buku(inventaris, judul, penulis, harga , stok):
    buku = {"judul": judul,
            "penulis": penulis,
            "harga": harga,
            "stok": stok}
    inventaris.append(buku)
    print(f'Buku "{judul}" berhasil ditambahkan!')

def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)
    if len(hasil) == 0:
        print('Buku tidak ditemukan.')
    else:
        print(f'Ditemukan {len(hasil)} buku')
        for i, buku in enumerate(hasil, start=1):
            print(f"{i}. {buku["judul"]} - {buku["penulis"]} | Rp{buku["harga"]} | stok: {buku["stok"]}")

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0 :
                print(f'Gagal! Stok tidak cukup. Stok "{buku["judul"]}" saat ini: {buku["stok"]}')
            else:
                buku["stok"] = stok_baru
                if jumlah >= 0:
                    print(f'Stok "{buku["judul"]}" bertambah {jumlah}. Stok sekarang: {buku["stok"]}')
                else:
                    print(f'Stok "{buku["judul"]}" berkurang {abs(jumlah)}. Stok sekarang: {buku["stok"]}')
            return
    print(f'Error: Buku "{judul}" tidak ditemukan')

def ringkasan_inventaris(inventaris):
    jumlah_jenis = len(inventaris)
    total_stok = 0
    total_aset = 0
    termahal = None

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]
        if termahal is None or buku["harga"] > termahal["harga"]:
            termahal = buku

    print('='*40)
    print('RINGKASAN INVENTARIS BOOKNEST')
    print('='*40)
    print(f'Jumlah jenis buku   : {jumlah_jenis}')            
    print(f'Total seluruh stok  : {total_stok}')
    print(f'Total nilai aset    : {total_aset}')
    if termahal is None:
        print('Buku termahal    : -')
    else:
        print(f'Buku termahal   : {termahal["judul"]} (Rp{termahal["harga"]})')
    print('='*40)

def tampilkan_menu():
    print('\nMenu:')
    print('1. Tambah Buku')
    print('2. Cari Buku')
    print('3. Update Stok')
    print('4. Ringkasan Inventaris')
    print('5. Keluar')

def menu_tambah_buku(inventaris):
    judul = input('Judul buku: ').strip()
    penulis = input('Penulis: ')

    try:
        harga = int(input('Harga: '))
        stok = int(input('Stok awal: '))
    except:
        print('Error: Harga dan stok harus berupa angka!')
        return

    if harga < 0 or stok < 0:
        print('Error: Harga dan stok tidak boleh negatif!')
        return

    tambah_buku(inventaris, judul, penulis, harga, stok)

def menu_update_stok(inventaris):
    judul = input('Judul buku yang ingin diupdate: ')
    try:
        jumlah = int(input('Jumlah perubahan (positif=tambah, negatif=kurang): '))
    except ValueError:
        print('Error: Jumlah perubahan harus berupa angka!')
        return

    update_stok(inventaris, judul, jumlah)

inventaris = []

print('=' * 30)
print('SISTEM INVETARIS BUKU BOOKNEST')
print('=' * 30)

while True:
    tampilkan_menu()
    pilihan = input('Pilih menu (1-5): ')

    if pilihan == "1":
        menu_tambah_buku(inventaris)
    elif pilihan == "2":
        kata_kunci = input('Masukkan kata kunci judul: ')
        cari_buku(inventaris, kata_kunci)
    elif pilihan == "3":
        menu_update_stok(inventaris)
    elif pilihan == "4":
        ringkasan_inventaris(inventaris)
    elif pilihan == "5":
        print('Terima kasih telah menggunakan BookNest!')
        break
    else:
        print('Pilihan tidak valid! Silahkan pilih 1-5.')

