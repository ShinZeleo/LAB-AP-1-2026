ALFABET = "abcdefghijklmnopqrstuvwxyz"

#Huruf bersih, menyimpan hanya huruf, lalu diubah ke huruf kecil
def bersihkan_teks(teks):
    hasil = ""
    for ch in teks:
        if ch.lower() in ALFABET:
            hasil += ch.lower()
    return hasil

#Validasi polinrom
def cek_palinrome(teks):
    terbalik = "".join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    for i in range(len(teks)):
        if teks[i] != terbalik[i]:
            return (False, i)

#Pencarian polinrom terpanjang
def inti_palinrome(teks):
    bersih = bersihkan_teks(teks)
    terbaik = {"teks": "", "panjang": 0, "indeks_awal": -1}

    for i in range(len(bersih)):
        for j in range(i + 1, len(bersih) + 1):
            sub = bersih[i:j]
            if len(sub) > terbaik["panjang"] and cek_palinrome(sub)[0]: #agar yang diawal tetap dipilih saat seri
                terbaik = {"teks": sub, "panjang": len(sub), "indeks_awal": i}

    return terbaik

#Input dan Output
def main():
    teks = input("Masukkan teks prasasti: ")
    print()
    print("Teks Bersih:", bersihkan_teks(teks))
    print("Output Terharap:", inti_palinrome(teks))

main()