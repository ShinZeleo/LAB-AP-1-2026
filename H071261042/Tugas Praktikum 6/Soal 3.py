#PROCESSING PROGRAM
#Program Untuk Menentukan Durasi(Detik)
def format_durasi(detik):
    return f"{detik // 60}:{detik % 60:02d}" #menghitung durasi dalam menit dan sisanya akan dibuat angka 2 digit dgn nol didepan

#Program Untuk Menambahkan Lagu
def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    for g in genre_set:
        if g.lower() == genre.lower():
            genre = g #genre sama, tidak ditambahkan
            break
    lagu = (judul, artis, genre, durasi) 
    playlist.append(lagu)
    genre_set.add(genre) #genre baru ditambahkan
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

#Program Untuk Menampilkan Playlist
def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong.")
        return
    garis = "=" * 70
    print(garis)
    print(f"{'No':<4}{'Judul':<25}{'Artis':<18}{'Genre':<10}{'Durasi':>7}") #jarak tampilan pada display
    print(garis)
    total = 0
    for i, (judul, artis, genre, durasi) in enumerate(playlist, 1): #mengurutkan musik dimulai dari 1
        print(f"{i:<4}{judul:<25}{artis:<18}{genre:<10}{format_durasi(durasi):>7}")
        total += durasi #total durasi playlist
    print(garis)
    print(f"Total durasi playlist: {total // 60} menit {total % 60} detik")

#Program Untuk Memfilter Genre
def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()] #memilih hanya sesuai pilihan genre

#Program Untuk Menghapus Lagu
def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        lagu = playlist.pop(nomor - 1) #untuk menghapus lagu sesuai pilihan nomor
        print(f"Lagu '{lagu[0]}' berhasil dihapus!")
        return lagu
    print("Error: Nomor lagu tidak valid!")
    return None

#Program Untuk Menampilkan Statistik Playlist
def statistik_playlist(playlist, genre_set):
    print("=" * 40)
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    if not playlist:
        print(" Playlist masih kosong.")
        print("=" * 40)
        return

    distribusi = {}
    for _, _, genre, _ in playlist:
        distribusi[genre] = distribusi.get(genre, 0) + 1 #menghitung jenis genre

    terpanjang = max(playlist, key=lambda lagu: lagu[3])
    terpendek = min(playlist, key=lambda lagu: lagu[3])

    print(f" Total lagu : {len(playlist)}")
    print(f" Jumlah genre : {len(genre_set)}")
    print(f" Daftar genre : {genre_set}")
    print(" Distribusi genre:")
    for genre, jumlah in distribusi.items():
        print(f"  {genre} : {'#' * jumlah} ({jumlah})")
    print(f" Lagu terpanjang : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f" Lagu terpendek : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("=" * 40)

#INPUT DAN OUTPUT PROGRAM
#Program Untuk Menampilkan Menu
def tampilkan_menu():
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

#Program Utama
def main():
    playlist = []
    genre_set = set()

    print("=" * 40)
    print(" PLAYLIST MUSIK - PLAYTUNE")
    print("=" * 40)

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            judul = input("Judul lagu: ").strip()
            artis = input("Artis: ").strip()
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    raise ValueError
            except ValueError:
                print("Error: Durasi harus berupa angka positif!")
                continue
            tambah_lagu(playlist, genre_set, judul, artis, genre, durasi) #program untuk menambahkan lagu

        elif pilihan == "2":
            tampilkan_playlist(playlist) #program untuk menampilkan playlist

        elif pilihan == "3":
            if not playlist:
                print("Playlist masih kosong.")
                continue
            print(f"Genre tersedia: {genre_set}")
            target = input("Masukkan genre yang ingin difilter: ").strip()
            hasil = filter_genre(playlist, target)
            if hasil:
                print(f"Lagu bergenre '{target}':")
                for i, (judul, artis, _, durasi) in enumerate(hasil, 1): #mengurutkan dimulai dari 1
                    print(f" {i}. {judul} - {artis} ({format_durasi(durasi)})")
            else:
                print(f"Tidak ada lagu bergenre '{target}'.")

        elif pilihan == "4":
            if not playlist:
                print("Playlist masih kosong.")
                continue
            tampilkan_playlist(playlist)
            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
            except ValueError:
                print("Error: Nomor harus berupa angka!")
                continue
            if hapus_lagu(playlist, nomor) is not None: #memperbarui set genre agar genre yang sudah tidak dipakai ikut hilang
                genre_set.clear()
                genre_set.update(lagu[2] for lagu in playlist)

        elif pilihan == "5":
            statistik_playlist(playlist, genre_set) #program untuk menampilkan statistik playlist

        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break

        else:
            print("Pilihan tidak valid. Masukkan angka 1-6.")

main()