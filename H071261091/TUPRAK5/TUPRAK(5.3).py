def cek_sandi(huruf, geser):
    ALFABET = "abcdefghijklmnopqrstuvwxyz"
    posisi_huruf = ALFABET.find(huruf.lower())
    if posisi_huruf == -1:
        return huruf

    posisi_baru = (posisi_huruf + geser) % 26
    huruf_baru = ALFABET[posisi_baru]

    if huruf == huruf.upper():
        return huruf_baru.upper()
    return huruf_baru.lower()


def mesin_enkripsi(teks, geser):
    teks_hasil = ""
    for huruf in teks:
        teks_hasil += cek_sandi(huruf, geser)
    return teks_hasil


def mesin_dekripsi(teks, geser):
    return mesin_enkripsi(teks, -geser)


def retas_sandi(sandi, kata_kunci):
    daftar_hasil = []

    for kunci in range(26):
        pesan_asli = mesin_dekripsi(sandi, kunci)
        if pesan_asli.lower().find(kata_kunci.lower()) != -1:
            daftar_hasil.append((kunci, pesan_asli))
    return daftar_hasil


sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")
print(f"\nOutput Deskripsi: {retas_sandi(sandi, kata_kunci)}")