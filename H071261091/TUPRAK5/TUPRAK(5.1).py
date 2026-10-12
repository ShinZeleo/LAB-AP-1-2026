def bersihkan_teks (teks):
    ALFABET = "abcdefghijklmnopqrstuvwxyz"
    teks_bersih = ""

    for huruf in teks:
        teks_lower = huruf.lower()
        if teks_lower in ALFABET:
            teks_bersih += teks_lower
    return teks_bersih

def cek_palindrom (teks):
    teks_dibalik = "".join(reversed(teks))
    if teks == teks_dibalik:
        return (True, -1)

    for i in range(len(teks)):
        if teks[i] != teks_dibalik[i]:
            return (False, i)

def inti_palindrom (teks):
    teks_bersih = bersihkan_teks(teks)
    n = len(teks_bersih)

    panjang_subteks = 0
    palindrom_subteks = ""
    palindrom_indeks = ""

    for i in range(n):
        for j in range (i + 1, n + 1):
            subteks = teks_bersih [i:j]
            adalah_palindrom = cek_palindrom(subteks)
            if adalah_palindrom[0] and len(subteks) > panjang_subteks:
                panjang_subteks = len(subteks)
                palindrom_subteks = subteks
                palindrom_indeks = i
    return {"teks": palindrom_subteks, "panjang": panjang_subteks, "indeks_awal": palindrom_indeks}


teks = input ("Masukkan teks prasasti: ")
print (f"Teks Bersih: {bersihkan_teks(teks)}")
print (f"Output Terharap: {inti_palindrom(teks)}")