DAFTAR_GENRE = ['Pop', 'Rock', 'Jazz', 'Rnb', 'Dangdut']


def format_durasi(detik):
    return f'{detik // 60}:{detik % 60:02d}'


def nama_bersih_genre(genre):
    genre = genre.strip()
    for g in DAFTAR_GENRE:
        if g.lower() == genre.lower():
            return g
    return genre.title()


def format_genre(playlist, genre_set):
    urutan = []
    for lagu in playlist:
        if lagu[2] in genre_set and lagu[2] not in urutan:
            urutan.append(lagu[2])
    return '{' + ', '.join(repr(g) for g in urutan) + '}'


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    genre = nama_bersih_genre(genre)
    lagu = (judul.strip(), artis.strip(), genre, durasi)

    playlist.append(lagu)
    genre_set.add(genre)
    print(f'Lagu "{lagu[0]}" oleh {lagu[1]} berhasil ditambahkan!')


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("\nPlaylist masih kosong")
        return

    print()
    print("="*55)
    print(f' {"No":<3} {"Judul":<19} {"Artis":<14} {"Genre":<9} Durasi')
    print("="*55)

    total = 0
    for i, (judul, artis, genre, durasi) in enumerate(playlist, start=1):
        print(f' {i:<3} {judul:<19} {artis:<14} {genre:<9} {format_durasi(durasi)}')
        total += durasi

    print("="*55)
    print(f' Total durasi playlist: {total // 60} menit {total % 60} detik')


def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.strip().lower()]


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Error: Nomor lagu tidak valid!")
        return None

    lagu = playlist.pop(nomor - 1)
    print(f'Lagu "{lagu[0]}" oleh {lagu[1]} berhasil dihapus!')
    return lagu


def statistik_playlist(playlist, genre_set):
    print()
    print("="*40)
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("="*40)

    if len(playlist) == 0:
        print(" Playlist masih kosong.")
        print("="*40)
        return

    print(f' {"Total lagu":<16}: {len(playlist)}')
    print(f' {"Jumlah genre":<16}: {len(genre_set)}')
    print(f' {"Daftar genre":<16}: {format_genre(playlist, genre_set)}')

    distribusi = {}
    for lagu in playlist:
        genre = lagu[2]
        distribusi[genre] = distribusi.get(genre, 0) + 1

    print("\n Distribusi genre:")
    for genre, jumlah in distribusi.items():
        print(f'    {genre:<12}: {"#"*jumlah} ({jumlah})')

    terpanjang = playlist[0]
    terpendek = playlist[0]
    for lagu in playlist:
        if lagu[3] > terpanjang[3]:
            terpanjang = lagu
        if lagu[3] < terpendek[3]:
            terpendek = lagu

    print(f"\n {'Lagu terpanjang':<16}: {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f" {'Lagu terpendek':<16}: {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("=" * 40)


def menu_musik():
    print('\nMenu:')
    print('1. Tambah Lagu')
    print('2. Tampilkan Playlist')
    print('3. Filter berdasarkan Genre')
    print('4. Hapus Lagu')
    print('5. Statistik Playlist')
    print('6. Keluar')


def menu_tambah_lagu(playlist, genre_set):
    judul = input("Judul lagu: ")
    artis = input("Artis: ")
    genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")

    try:
        durasi = int(input("Durasi (dalam detik): "))
    except ValueError:
        print("Error: Durasi harus berupa angka positif!")
        return

    tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)


def menu_filter_genre(playlist, genre_set):
    if len(genre_set) == 0:
        print("Playlist masih kosong, belum ada genre.")
        return

    print(f'Genre tersedia: {format_genre(playlist, genre_set)}')
    genre = input("Masukkan genre yang ingin difilter: ")

    hasil = filter_genre(playlist, genre)
    genre_tampil = nama_bersih_genre(genre)

    if len(hasil) == 0:
        print(f'\nTidak ada lagu bergenre "{genre_tampil}".')
    else:
        print(f'\nLagu bergenre "{genre_tampil}":')
        for i, (judul, artis, _, durasi) in enumerate(hasil, start=1):
            print(f'    {i}. {judul} - {artis} ({format_durasi(durasi)})')


def menu_hapus_lagu(playlist, genre_set):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    tampilkan_playlist(playlist)
    try:
        nomor = int(input("\nNomor lagu yang ingin dihapus: "))
    except:
        print("Error: Nomor harus berupa angka!")
        return

    if hapus_lagu(playlist, nomor):
        genre_set.clear()
        genre_set.update(lagu[2] for lagu in playlist)


playlist = []
genre_set = set()

print("=" * 40)
print("   PLAYLIST MUSIK - PLAYTUNE")
print("=" * 40)
menu_musik()
 
while True:
    pilihan = input("Pilih menu (1-6): ")
 
    if pilihan == "1":
        menu_tambah_lagu(playlist, genre_set)
    elif pilihan == "2":
        tampilkan_playlist(playlist)
    elif pilihan == "3":
        menu_filter_genre(playlist, genre_set)
    elif pilihan == "4":
        menu_hapus_lagu(playlist, genre_set)
    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)
    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih 1-6.")
 
    print()