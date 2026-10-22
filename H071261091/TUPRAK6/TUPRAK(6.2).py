def daftar_kandidat(kandidat_set, nama):
    nama_kapital = nama.capitalize()
    if nama_kapital in kandidat_set:
        print(f"Kandidat '{nama_kapital}' sudah terdaftar!")
    else:
        kandidat_set.add(nama_kapital)
        print(f"'{nama_kapital}' berhasil didaftarkan sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih_lower = nama_pemilih.lower()
    pilihan_kapital = pilihan.capitalize()
    
    if pemilih_lower in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return
    
    if pilihan_kapital not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak terdaftar!")
        return
    
    rekap_suara[pemilih_lower] = pilihan_kapital
    print(f"Suara '{nama_pemilih}' untuk '{pilihan_kapital}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0
        
    for _, pilihan in rekap_suara.items():
        if pilihan in perolehan:
            perolehan[pilihan] += 1
            
    return perolehan

def tampilkan_hasil(perolehan):
    total_suara = 0
    max_suara = -1
    pemenang = []
    
    print("\n========================================")
    print("HASIL PEMILIHAN KETUA KELAS")
    print("========================================")
    for kandidat, jumlah in perolehan.items():
        print(f"{kandidat}: {jumlah} suara")
        total_suara += jumlah
        
        if jumlah > max_suara:
            max_suara = jumlah
            pemenang = [kandidat]
        elif jumlah == max_suara:
            pemenang.append(kandidat)
            
    print(f"Total suara masuk: {total_suara}")
    
    if len(pemenang) > 1:
        print(f"Hasil SERI antara: {', '.join(pemenang)}")
        print("Perlu dilakukan pemilihan ulang!")
    elif len(pemenang) == 1 and max_suara > 0:
        print(f"PEMENANG: {pemenang[0]} dengan {max_suara} suara!")
    else:
        print("Belum ada suara yang masuk.")
    print("========================================")

kandidat_set = set()
rekap_suara = {}

print("========================================")
print("SISTEM PEMILIHAN KETUA KELAS")
print("========================================")
print("FASE PENDAFTARAN KANDIDAT")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
    if nama == "":
        if len(kandidat_set) < 2:
            print("Peringatan: Minimal harus ada 2 kandidat sebelum bisa lanjut!")
            continue
        else:
            break
    daftar_kandidat(kandidat_set, nama)

print(f"Kandidat terdaftar: {kandidat_set}")

print("\nFASE PEMUNGUTAN SUARA")
while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
    if nama_pemilih == "":
        break
    print(f"Kandidat yang tersedia: {kandidat_set}")
    pilihan = input("Pilih kandidat: ")
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

perolehan_suara = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan_suara)