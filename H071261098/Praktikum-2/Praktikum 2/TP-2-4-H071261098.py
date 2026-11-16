tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").capitalize()
waktu = input("Masukkan waktu (Pagi/Malam): ").capitalize()
pengunjung = input("Masukkan tipe pengunjung (Anak/Dewasa): ").capitalize()

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            paket = "Paket A"
    

    case "Pegunungan":
        if waktu == "Pagi" and pengunjung == "Dewasa":
            paket = "Paket B"
        

    case "Kota":
        if waktu == "Malam":
            paket = "Paket C"
        

    case _:
        paket = "Tidak ada paket yang cocok"

print (f"Paket Rekomendasi: {paket}")
