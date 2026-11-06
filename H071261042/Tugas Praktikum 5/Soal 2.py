ALFABET = "abcdefghijklmnopqrstuvwxyz"

#List indeks kemunculan kata
def cek_kata(teks, kata):
    indeks = []
    if kata == "":
        return indeks

    teks_kecil = teks.lower()
    kata_kecil = kata.lower()

    start = 0
    while True:
        pos = teks_kecil.find(kata_kecil, start)
        if pos == -1:
            break
        indeks.append(pos)
        start = pos + 1
    return indeks

#Mengecek batas kata (berdiri sendiri atau tidak)
def cek_batas_kata(teks, i, panjang):
    if i > 0 and teks[i - 1].lower() in ALFABET:
        return False #karakter sebelum kata
    akhir = i + panjang
    if akhir < len(teks) and teks[akhir].lower() in ALFABET:
        return False #karakter sesudah kata
    return True #kata berdiri sendiri

#Menyensor kata
def sensor_kata(teks, kata, simbol):
    panjang = len(kata)
    pengganti = simbol[0] * panjang if simbol != "" else "*" * panjang
    
    indeks_awal = [] #indeks awal kata yang berdiri sendiri
    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, panjang):
            indeks_awal.append(i)

    hasil = ""
    pos = 0
    for i in indeks_awal:
        hasil = hasil + teks[pos:i] + pengganti
        pos = i + panjang
    hasil = hasil + teks[pos:]
    return (hasil, len(indeks_awal), indeks_awal) #hasil teks yang disensor

#Input dan Output
def main():
    teks = input("Masukkan Teks: ")
    kata = input("Masukkan kata target: ")
    simbol = input("Masukkan simbol: ")

    hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
    print("Hasil Teks:", hasil)
    print("Jumlah:", jumlah, "| Indeks:", indeks)

main()