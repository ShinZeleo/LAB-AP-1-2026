#Input kursi
while True:
    try:
        sisa_kursi = int(input("Masukkan maksimal kursi bus: "))
    except ValueError:
        print("Input jumlah kursi harus berupa angka!")
        continue
    if sisa_kursi <= 0:
        print("Jumlah kursi harus lebih dari 0!")
        continue
    break

#Processing program
print("--- Sistem Reservasi PO BUS Dimulai ---")
total_pendapatan = 0

while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")
    try: #Input umur
        umur = int(input("Masukkan umur penumpang: "))
    except ValueError:
        print("Input umur harus berupa angka!")
        continue #tidak berkurang

    #Penentuan harga
    if umur < 0:
        print("Umur tidak valid!")
        continue #tidak berkurang
    if umur <= 5:
        harga = 0
        kategori = "Balita - Gratis (Rp 0)"
    elif umur <= 12:
        harga = 50000
        kategori = "Anak - Harga: Rp 50.000"
    else:
        harga = 100000
        kategori = "Dewasa - Harga: Rp 100.000"
    print(f"Kategori: {kategori}\n")

    #Total pendapatan
    total_pendapatan += harga
    sisa_kursi -= 1

#End
print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")
