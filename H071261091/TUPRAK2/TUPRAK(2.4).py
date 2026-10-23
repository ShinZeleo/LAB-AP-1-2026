tujuan = input("Masukkan Tujuan (Pantai/Pegunungan/Kota): ").capitalize()
waktu = input("Masukkan Waktu (Pagi/Malam): ").capitalize()
tipe_pengunjung = input("Masukkan Tipe Pengunjung (Anak/Dewasa): ").capitalize()

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            print ("Paket Rekomendasi: Paket A")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            print ("Paket Rekomendasi: Paket C")
        else:
            print ("Tidak Ada Paket yang Cocok")
    case "Pegunungan":
        if waktu == "Pagi" and tipe_pengunjung == "Dewasa":
            print ("Paket Rekomendasi: Paket B")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            print ("Paket Rekomendasi: Paket C")
        else:
            print ("Tidak Ada Paket yang Cocok")
    case "Kota":
        if waktu == "Malam":
            print ("Paket Rekomendasi: Paket C")
        else:
            print ("Tidak Ada Paket yang Cocok")
    case _:
        print ("Tidak Ada Paket yang Cocok")