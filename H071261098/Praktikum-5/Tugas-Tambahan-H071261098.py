# Meminta input kata dari pengguna
kata = input("Masukkan kata : ")


if len(kata) > 0:
    karakter_pertama = kata[0]
    
    
    indeks_tengah = len(kata) // 2
    karakter_tengah = kata[indeks_tengah]
    
    karakter_terakhir = kata[-1]

    
    hasil = karakter_pertama + karakter_tengah + karakter_terakhir
    
    print(hasil)
else:
    print("Input tidak boleh kosong.")