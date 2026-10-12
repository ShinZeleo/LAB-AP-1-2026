ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    teks_bersih = ""
    for karakter in teks:
        karakter_kecil = karakter.lower()
        if karakter_kecil in ALFABET:
            teks_bersih += karakter_kecil
    return teks_bersih

def cek_palinrome(teks):
    teks_dibalik = "".join(reversed(teks))
    if teks == teks_dibalik:
        return (True, -1)
    
    for i in range(len(teks)):
        if teks[i] != teks_dibalik[i]:
            return (False, i)
    return (False, 0)

def inti_palinrome(teks):
    teks_bersih = bersihkan_teks(teks)
    panjang_text_bersih = len(teks_bersih)
    
    palindrom_terpanjang = 0
    simpan_palindrom_terpanjang = ""
    index_palindrom_terpanjang = 0
    
    for i in range(panjang_text_bersih):
        for j in range(i + 1, panjang_text_bersih + 1):
            pemotongan_string = teks_bersih[i:j]
            apakah_palindrom, _ = cek_palinrome(pemotongan_string)
            if apakah_palindrom:
                if len(pemotongan_string) > palindrom_terpanjang:
                    palindrom_terpanjang = len(pemotongan_string)
                    simpan_palindrom_terpanjang = pemotongan_string
                    index_palindrom_terpanjang = i
                    
    return {
        "teks": simpan_palindrom_terpanjang,
        "panjang": palindrom_terpanjang,
        "indeks_awal": index_palindrom_terpanjang
    }

kata = input("Masukkan teks: ")
kata_bersih = bersihkan_teks(kata)
keluaran = inti_palinrome(kata)
print(f"Teks Bersih: {kata_bersih}")
print(f"Output Terharap: {keluaran}")