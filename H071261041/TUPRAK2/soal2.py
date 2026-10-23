jarak = int(input("Masukkan jarak pengirim (km): "))
express = input("Layanan express (ya/tidak): ").lower()
if jarak < 5:
    tarif_dasar = 10000
elif jarak <= 20:
    tarif_dasar = 20000
else:
    tarif_dasar = 35000

layanan = 15000 if express == "ya" else 0 
total = tarif_dasar + layanan 
print ("Total Tarif Pengiriman: Rp", total)