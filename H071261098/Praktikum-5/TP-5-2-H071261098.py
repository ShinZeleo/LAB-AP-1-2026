def cek_kata(teks, kata):
    indeks = []
    teks_lower = teks.lower()
    kata_lower = kata.lower()
    start = 0
    
    while True:
        cari_kata = teks_lower.find(kata_lower, start)
        if cari_kata == -1:
            break
        indeks.append(cari_kata)
        start = cari_kata + 1
    return indeks

def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sebelum_ok = True
    sesudah_ok = True
    
    
    if i > 0:
        if teks[i - 1] in alfabet:
            sebelum_ok = False
                
    
    if i + panjang < len(teks):
        if teks[i + panjang] in alfabet:
            sesudah_ok = False
            
    return sebelum_ok and sesudah_ok

def sensor_kata(teks, kata, simbol):
    indeks_awal_mentah = cek_kata(teks, kata)
    indeks_valid = []
    
    for i in indeks_awal_mentah:
        if cek_batas_kata(teks, i, len(kata)):
            indeks_valid.append(i)
            
    teks_tersensor = ""
    cari_kata = 0
    panjang = len(kata)
    
    
    for i in indeks_valid:
        teks_tersensor += teks[cari_kata:i]
        teks_tersensor += simbol * panjang
        cari_kata = i + panjang
        
    teks_tersensor += teks[cari_kata:]
    
    return teks_tersensor, len(indeks_valid), indeks_valid

teks = input("Masukkan Teks: ")
kata_target = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")
    
hasil_teks, jumlah, daftar_indeks = sensor_kata(teks, kata_target, simbol)
print(f"Hasil Teks: {hasil_teks}")
print(f"Jumlah: {jumlah}  Indeks: {daftar_indeks}")