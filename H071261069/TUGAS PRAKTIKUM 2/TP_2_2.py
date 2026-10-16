# TASK II
print("=== HARGA JARAK PENGIRIMAN ===")
print("Jarak di bawah 5 km : Rp10.000")
print("Jarak 5 - 20 km : Rp20.000")
print("Jarak di atas 20 km : Rp35.000")

jarak_kirim = float(input("\nMasukkan jarak pengiriman (km) : " ))
layanan_express = input("Layanan express (Ya/Tidak) : ").capitalize()  

if jarak_kirim <= 0:
    print("Invalid, Masukkan ulang jarak")
elif jarak_kirim < 5:
    harga = 10000
elif jarak_kirim <= 20 :
    harga = 20000
else:
    harga = 35000

biaya_tambahan = 15000 if layanan_express == "Ya" else 0

total_harga = harga + biaya_tambahan

print(("Harga total : Rp"), total_harga)