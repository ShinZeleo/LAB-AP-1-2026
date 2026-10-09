def awal_tengah_akhir(kata):
    if kata == "":
        return ""

    indeks_tengah = len(kata) // 2
    karakter_awal = kata[0]
    karakter_tengah = kata[indeks_tengah]
    karakter_akhir = kata[-1]
    return karakter_awal + karakter_tengah + karakter_akhir

kata = input("Masukkan kata : ")
print(awal_tengah_akhir(kata))