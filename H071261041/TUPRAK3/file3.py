while True:
    try:
        total_kursi = int(input("Masukkan maksimal kursi bus: "))
        if total_kursi <= 0: 
            print("Jumlah kursi harus lebih dari 0!")
        else:
            break
    except ValueError:  
        print("Input jumlah kursi harus berupa angka!")

sisa_kursi = total_kursi
total_pendapatan = 0

print("---Sistem Reservasi PO BUS Dimulai---")

while sisa_kursi > 0: 
    print(f"Sisa kursi: {sisa_kursi}")
    try:
        umur = int(input("Masukkan umur penumpang: "))

        if umur < 0: 
            print("umur tidak valid")
            continue

        if 0 <= umur <= 5: 
            kategori = "Balita"
            harga = 0
            print(f"Kategori: {kategori} - Tiket Gratis (Rp {harga})")
        elif 6 <= umur <= 12: 
            kategori = "Anak"
            harga = 50000
            print(f"Kategori: {kategori} Harga: Rp {harga:,}")
        else: 
            kategori = "Dewasa"
            harga = 100000
            print(f"Kategori: {kategori} Harga:  Rp {harga:,}")

        total_pendapatan += harga
        sisa_kursi -= 1

    except ValueError: 
        print("Input umur harus berupa angka!")

print("---Semua kursi terisi---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}") 