#Tugas no 2
jarak = int(input("Masukkan jarak pengiriman (km): "))
express = input("Layanan Express (ya/tidak): ").lower()

if jarak <5 :
    jarak = 10000
elif jarak >=5 and jarak  <=20:
    jarak = 20000
else :
    jarak = 35000

biaya_layanan = 15000 if express == "ya" else 0
tarif = jarak + biaya_layanan
print ("Total tarif pengiriman: Rp", tarif)
