ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    if ch.lower() in ALFABET:
        posisi_awal = ALFABET.find(ch.lower())
        posisi_baru = (posisi_awal + k) % 26
        karakter_baru = ALFABET[posisi_baru]
        
        if ch.isupper():
            return karakter_baru.upper()
        else:
            return karakter_baru
    return ch
    
def mesin_enkripsi(teks, k):
    hasil = ""
    for i in teks:
        hasil += cek_sandi(i, k)
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)
        
def retas_sandi(sandi, kata_kunci):
    hasil_peretasan = []
    
    for k in range(26):

        pesan_kemungkinan = mesin_dekripsi(sandi, k)
            
        if pesan_kemungkinan.find(kata_kunci) != -1:
            hasil_peretasan.append((k, pesan_kemungkinan))
                
    return hasil_peretasan


sandi_input = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci_input = input("Masukkan kata kunci target: ")

hasil_akhir = retas_sandi(sandi_input, kata_kunci_input)
print(f"Output Deskripsi: {hasil_akhir}")