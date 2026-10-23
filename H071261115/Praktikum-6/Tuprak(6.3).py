def format_durasi(detik):
    """Mengubah detik menjadi format menit:detik (contoh: 354 -> 5:54)."""
    menit, sisa = divmod(detik, 60)
    return f"{menit}:{sisa:02d}"


def urut_genre(playlist, genre_set):
    """Mengurutkan genre sesuai kemunculan pertama di playlist (agar tampilan konsisten)."""
    return list(dict.fromkeys(lagu[2] for lagu in playlist if lagu[2] in genre_set))


def format_set(playlist, genre_set):
    """Menampilkan set genre dalam format {'Rock', 'Pop', ...}."""
    return "{" + ", ".join(repr(g) for g in urut_genre(playlist, genre_set)) + "}"


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    """Menambahkan lagu (tuple) ke playlist dan genre-nya ke set."""
   
    for g in genre_set:
        if g.lower() == genre.lower():
            genre = g
            break

    lagu = (judul, artis, genre, durasi)  
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    """Menampilkan seluruh lagu dalam bentuk tabel sederhana + total durasi."""
    print()
    if not playlist:
        print("Playlist masih kosong.")
        return

    w_judul = max(18, max(len(l[0]) for l in playlist))
    w_artis = max(13, max(len(l[1]) for l in playlist))
    w_genre = max(8, max(len(l[2]) for l in playlist))
    lebar = 5 + w_judul + 2 + w_artis + 2 + w_genre + 2 + 6
    garis = "=" * lebar

    print(garis)
    print(f" {'No':<2}  {'Judul':<{w_judul}}  {'Artis':<{w_artis}}  "
          f"{'Genre':<{w_genre}}  Durasi")
    print(garis)
    for i, (judul, artis, genre, durasi) in enumerate(playlist, start=1):
        print(f" {i:<2}  {judul:<{w_judul}}  {artis:<{w_artis}}  "
              f"{genre:<{w_genre}}  {format_durasi(durasi)}")
    print(garis)

    total = sum(lagu[3] for lagu in playlist)
    menit, detik = divmod(total, 60)
    print(f" Total durasi playlist: {menit} menit {detik} detik")


def filter_genre(playlist, genre_target):
    """Mengembalikan list lagu dengan genre tertentu (list comprehension)."""
    return [lagu for lagu in playlist
            if lagu[2].lower() == genre_target.strip().lower()]


def hapus_lagu(playlist, nomor):
    """Menghapus lagu berdasarkan nomor urut (pakai pop() dengan indeks)."""
    if 1 <= nomor <= len(playlist):
        return playlist.pop(nomor - 1)
    return None


def statistik_playlist(playlist, genre_set):
    """Menampilkan statistik playlist."""
    garis = "=" * 40
    print()
    print(garis)
    print("  STATISTIK PLAYLIST PLAYTUNE")
    print(garis)

    if not playlist:
        print("  Playlist masih kosong.")
        print(garis)
        return

    
    distribusi = {}
    for lagu in playlist:
        genre = lagu[2]
        distribusi[genre] = distribusi.get(genre, 0) + 1

    terpanjang = max(playlist, key=lambda lagu: lagu[3])
    terpendek = min(playlist, key=lambda lagu: lagu[3])

    print(f"  {'Total lagu':<16}: {len(playlist)}")
    print(f"  {'Jumlah genre':<16}: {len(genre_set)}")
    print(f"  {'Daftar genre':<16}: {format_set(playlist, genre_set)}")
    print()
    print("  Distribusi genre:")
    for genre in urut_genre(playlist, genre_set):
        jumlah = distribusi[genre]
        print(f"    {genre:<12}: {'#' * jumlah} ({jumlah})")
    print()
    print(f"  {'Lagu terpanjang':<16}: {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f"  {'Lagu terpendek':<16}: {terpendek[0]} ({format_durasi(terpendek[3])})")
    print(garis)


def main():
    playlist = []
    genre_set = set()
    garis = "=" * 40

    print(garis)
    print("   PLAYLIST MUSIK - PLAYTUNE")
    print(garis)
    print()
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    while True:
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            judul = input("Judul lagu: ").strip()
            artis = input("Artis: ").strip()
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    print("Error! Durasi harus berupa angka positif.")
                elif not judul or not artis or not genre:
                    print("Error! Judul, artis, dan genre tidak boleh kosong.")
                else:
                    genre = genre[0].upper() + genre[1:]
                    tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            except ValueError:
                print("Error! Durasi harus berupa angka positif.")

        elif pilihan == "2":
            tampilkan_playlist(playlist)

        elif pilihan == "3":
            if not playlist:
                print("Playlist masih kosong.")
            else:
                print(f"Genre tersedia: {format_set(playlist, genre_set)}")
                target = input("Masukkan genre yang ingin difilter: ").strip()
                hasil = filter_genre(playlist, target)
                print()
                if not hasil:
                    print(f"Tidak ada lagu bergenre '{target}'.")
                else:
                    print(f"Lagu bergenre '{hasil[0][2]}':")
                    for i, (judul, artis, _, durasi) in enumerate(hasil, start=1):
                        print(f"  {i}. {judul} - {artis} ({format_durasi(durasi)})")

        elif pilihan == "4":
            if not playlist:
                print("Playlist masih kosong.")
            else:
                tampilkan_playlist(playlist)
                try:
                    nomor = int(input("Nomor lagu yang ingin dihapus: "))
                    lagu = hapus_lagu(playlist, nomor)
                    if lagu is None:
                        print("Error! Nomor lagu tidak valid.")
                    else:
                        print(f"Lagu '{lagu[0]}' berhasil dihapus!")
                        # Sinkronkan set genre dengan lagu yang tersisa
                        genre_set.clear()
                        genre_set.update(l[2] for l in playlist)
                except ValueError:
                    print("Error! Nomor lagu harus berupa angka.")

        elif pilihan == "5":
            statistik_playlist(playlist, genre_set)

        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break

        else:
            print("Pilihan tidak valid. Masukkan angka 1-6.")

        print()


if __name__ == "__main__":
    main()