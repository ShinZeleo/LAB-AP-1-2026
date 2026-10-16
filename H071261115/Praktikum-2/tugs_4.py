#Tugas no 4
tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").capitalize()
waktu = input("Masukkan waktu (Pagi/Malam): ").capitalize()
tipe = input("Masukkan tipe (Anak/Dewasa): ").capitalize()
match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            print ("paket rekomendasi : Paket A")
        elif waktu == "Malam" and tipe == "Dewasa":
            print ("paket rekomendasi : Paket c")
        else:
            print ("Tidak ada paket yang cocok")
    case "Pegunungan":
        if waktu == "Pagi" and tipe == "Dewasa":
            print("paket rekomendasi : Paket B")
        elif waktu == "Malam" and tipe == "Dewasa":
            print("paket rekomendasi : Paket C") 
        else:
            print("Tidak ada paket yang cocok")
    case "Kota":
        if waktu == "Malam":
            print("paket rekomendasi : Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case _: 
        print("Tidak ada paket yang cocok") 