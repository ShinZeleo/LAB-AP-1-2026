jarak = int(input("Masukkan Jarak Pengiriman (Km): "))
express = input("Layanan Express (Ya/Tidak): ").lower()

if jarak < 5: 
    tarif = 10000
elif jarak <= 20:
    tarif = 20000
else:
    tarif = 35000

biaya_tambahan = 15000 if express == "ya" else 0

tarif = tarif + biaya_tambahan

print("Total Tarif Pengiriman: Rp", tarif)