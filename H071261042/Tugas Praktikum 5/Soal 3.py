ALFABET = "abcdefghijklmnopqrstuvwxyz"

#Geser satu karakter sejauh k posisi (k boleh negatif / > 26)
def cek_sandi(ch, k):
    idx = ALFABET.find(ch.lower())
    if idx == -1: #karakter bukan huruf, tidak diubah
        return ch

    huruf_baru = ALFABET[(idx + k) % 26]

    if ch == ch.upper(): #pertahankan format huruf
        return huruf_baru.upper()
    return huruf_baru.lower()

#Mengubah seluruh teks dengan pergeseran k
def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch, k)
    return hasil

#Mengubah seluruh teks dengan pergeseran k yang berlawanan
def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

#Retas sandi Caesar dengan brute force, simpan hanya hasil yang memuat kata kunci
def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan))
    return hasil

#Input dan Output
def main():
    sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
    kata_kunci = input("Masukkan kata kunci target: ")
    print()
    print("Output Deskripsi:", retas_sandi(sandi, kata_kunci))

main()