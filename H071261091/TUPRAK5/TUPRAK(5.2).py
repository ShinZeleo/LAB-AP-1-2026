def cek_kata(teks, kata):
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    daftar_indeks = []

    posisi = teks_kecil.find(kata_kecil, 0)
    while posisi != -1:
        daftar_indeks.append(posisi)
        posisi = teks_kecil.find(kata_kecil, posisi + 1)
    return daftar_indeks

def bukan_huruf(karakter):
    ALFABET = "abcdefghijklmnopqrstuvwxyz"
    return karakter.lower() not in ALFABET

def cek_batas_kata(teks, posisi_awal, panjang_kata):
    posisi_setelah_kata = posisi_awal + panjang_kata
    
    if posisi_awal == 0:
        batas_kiri_aman = True
    else:
        batas_kiri_aman = bukan_huruf(teks[posisi_awal - 1])
    
    if posisi_setelah_kata == len(teks):
        batas_kanan_aman = True
    else:
        batas_kanan_aman = bukan_huruf(teks[posisi_setelah_kata])
    
    return batas_kiri_aman and batas_kanan_aman
    
    
def sensor_kata(teks, kata, simbol):
    panjang_kata = len(kata)
    teks_tersensor = ""
    daftar_indeks_sensor = []
    posisi_sudah_disalin = 0
    
    for posisi in cek_kata(teks, kata):
        if cek_batas_kata(teks, posisi, panjang_kata):
            bagian_sebelum_kata = teks[posisi_sudah_disalin:posisi]
            teks_tersensor = teks_tersensor + bagian_sebelum_kata + simbol * panjang_kata
            daftar_indeks_sensor.append(posisi)
            posisi_sudah_disalin = posisi + panjang_kata
    
    teks_tersensor = teks_tersensor + teks[posisi_sudah_disalin:]
    return (teks_tersensor, len(daftar_indeks_sensor), daftar_indeks_sensor)


teks = input("Masukkan Teks: ")
kata_target = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

teks_tersensor, jumlah_tersensor, daftar_indeks = sensor_kata(teks, kata_target, simbol)
print(f"Hasil Teks: {teks_tersensor}")
print(f"Jumlah: {jumlah_tersensor} | Indeks: {daftar_indeks}")