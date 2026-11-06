tujuan = input("masukkan tujuan (pantai/pegunungan/kota) :")
waktu = input("masukkan waktu (pagi/malam) :")
tipe = input("masukkan tipe pengunjung (anak/dewasa) :")

match tujuan : 
   case "pantai":
      if waktu == "pagi":
         print("paket rekomendasi: paket A")
      elif waktu == "malam" and tipe == "dewasa":
         print("paket rekomendasi: paket C")
      else:
         print("tidak ada paket yang cocok")
   case "pegunungan":
      if waktu == "pagi" and tipe == "dewasa":
         print("paket rekomendasi: paket B")
      elif waktu == "malam" and tipe == "dewasa":
         print("paket rekomendasi: paket C")
      else:
         print("tidak ada paket yang cocok")
   case "kota":
      if waktu == "malam":
         print("paket rekomendasi: paket C")
      else:
         print ("tidak ada paket yang cocok")
   case _:
      print("tidak ada paket yang cocok")