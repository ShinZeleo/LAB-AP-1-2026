def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print (f"lagu '{judul}' oleh '{artis}' berhasil di tambahkan!")

def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return
    
    print("===========================================================")
    print("No  Judul                  Artis          Genre    Durasi")
    print("===========================================================")
    
    total_detik = 0
    no = 1
    for lagu in playlist:
        judul, artis, genre, durasi = lagu
        total_detik += durasi
        
        menit = durasi // 60
        detik = durasi % 60
        if detik < 10:
            durasi_str = f"{menit}:0{detik}"
        else:
            durasi_str = f"{menit}:{detik}"
            
        print(f"{no:<3} {judul:<22} {artis:<14} {genre:<8} {durasi_str}")
        no += 1
        
    print("===========================================================")
    total_menit = total_detik // 60
    sisa_detik = total_detik % 60
    print(f"Total durasi playlist: {total_menit} menit {sisa_detik} detik")

def filter_genre(playlist, target):
    hasil_filter = [lagu for lagu in playlist if lagu[2].lower() == target.lower()]
    if len(hasil_filter) > 0:
        print (f"Lagu bergenre {target}:")
        no = 1
        for l in hasil_filter:
            menit = l[3] // 60
            detik = l[3] % 60
            if detik < 10:
                durasi_str = f"{menit}:0{detik}"
            else:
                durasi_str = f"{menit}:{detik}"
            print (f"{no}. {l[0]} - {l[1]} ({durasi_str})")
            no += 1
    else:
        print ("Tidak ada lagu dengan genre tsb.")

def hapus_lagu(playlist, nomor):
    indeks = nomor - 1
    if 0 <= indeks and indeks < len(playlist):
        lagu_terhapus = playlist.pop(indeks)
        print (f"Lagu '{lagu_terhapus[0]}' berhasil dihapus dari playlist.")
    else:
        print("Nomor lagu tidak valid!")

def statistik_playlist(playlist, genre_set):
    print("=========================================")
    print("       STATISTIK PLAYLIST PLAYTUNE       ")
    print("=========================================")

    if len(playlist) == 0:
        print("Playlist masih kosong, belum ada statistik.")
        return
        
    total_lagu = len(playlist)
    jumlah_genre = len(genre_set)
    
    distribusi = {}
    for genre in genre_set:
        distribusi[genre] = 0
        
    for lagu in playlist:
        genre_lagu = lagu[2]
        if genre_lagu in distribusi:
            distribusi[genre_lagu] += 1
            
    terpanjang = playlist[0]
    terpendek = playlist[0]
    
    for lagu in playlist:
        if lagu[3] > terpanjang[3]:
            terpanjang = lagu
        if lagu[3] < terpendek[3]:
            terpendek = lagu

    print(f"Total lagu      : {total_lagu}")
    print(f"Jumlah genre    : {jumlah_genre}")
    print(f"Daftar genre    : {genre_set}")
    print("Distribusi genre:")

    for genre, jumlah in distribusi.items():
        simbol = "#" * jumlah
        print(f"{genre:<15} : {simbol} ({jumlah})")
        
    m_panjang = terpanjang[3] // 60
    d_panjang = terpanjang[3] % 60
    durasi_panjang_str = f"{m_panjang}:0{d_panjang}" if d_panjang < 10 else f"{m_panjang}:{d_panjang}"
    
    m_pendek = terpendek[3] // 60
    d_pendek = terpendek[3] % 60
    durasi_pendek_str = f"{m_pendek}:0{d_pendek}" if d_pendek < 10 else f"{m_pendek}:{d_pendek}"
    
    print(f"Lagu terpanjang : {terpanjang[0]} ({durasi_panjang_str})")
    print(f"Lagu terpendek  : {terpendek[0]} ({durasi_pendek_str})")
    print("=========================================")

playlist_musik = []
genre_set = set()

while True:
    print ("\n======================================")
    print ("       PLAYLIST MUSIK - PLAYTUNE        ")
    print ("======================================\n")

    print ("Menu: ")
    print ("1. Tambah Lagu")
    print ("2. Tampilkan Playlist")
    print ("3. Filter berdasarkan Genre")
    print ("4. Hapus Lagu")
    print ("5. Statistik Playlist")
    print ("6. Keluar")

    menu = input("Pilih menu (1-6): ")

    if menu == "1":
            judul = input("Judul lagu: ").title()
            artis = input("Artis: ").title()
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").capitalize()
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                      print("Durasi harus berupa angka positif!")
                      continue
                else:
                    tambah_lagu(playlist_musik, genre_set, judul, artis, genre, durasi)
            except ValueError:
                print ("Durasi harus berupa bilangan bulat!")
    
    elif menu == "2":
        tampilkan_playlist(playlist_musik)

    elif menu == "3":
        print ("Genre tersedia: ", genre_set)
        target = input("Masukkan genre yang ingin difilter: ").capitalize()
        filter_genre(playlist_musik, target)
        

    elif menu == "4":
        tampilkan_playlist(playlist_musik)
        if len(playlist_musik) > 0:
            nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
            hapus_lagu(playlist_musik, nomor)
        
    elif menu == "5":
        statistik_playlist(playlist_musik, genre_set)

    elif menu == "6":
        print ("Terima kasih telah menggunakan PlayTune!")
        break