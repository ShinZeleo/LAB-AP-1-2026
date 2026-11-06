ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata):
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    hasil = []
    if kata_kecil == "":
        return hasil
    start = 0
    while True:
        i = teks_kecil.find(kata_kecil, start)
        if i == -1:
            break
        hasil.append(i)
        start = i + 1
    return hasil


def cek_batas_kata(teks, i, panjang):
    # karakter sebelum kata
    if i > 0 and teks[i - 1].lower() in ALFABET:
        return False
    # karakter sesudah kata
    akhir = i + panjang
    if akhir < len(teks) and teks[akhir].lower() in ALFABET:
        return False
    return True


def sensor_kata(teks, kata, simbol):
    panjang = len(kata)
    hasil = ""
    indeks_sensor = []
    posisi = 0  # teks asli sudah disalin sampai sini

    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, panjang):
            hasil += teks[posisi:i] + simbol * panjang
            posisi = i + panjang
            indeks_sensor.append(i)

    hasil += teks[posisi:]
    return (hasil, len(indeks_sensor), indeks_sensor)


if __name__ == "__main__":
    teks = input("Masukkan Teks: ")
    kata = input("Masukkan kata target: ")
    simbol = input("Masukkan simbol: ")
    tersensor, jumlah, indeks = sensor_kata(teks, kata, simbol)
    print("Hasil Teks:", tersensor)
    print("Jumlah:", jumlah, "| Indeks:", indeks)