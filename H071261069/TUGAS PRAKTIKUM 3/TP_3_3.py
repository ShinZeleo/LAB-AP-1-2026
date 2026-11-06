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

print("\n--- Sistem Reservasi PO BUS Dimulai ---")

total_pendapatan = 0

while sisa_kursi > 0:
    print(f"\nSisa kursi: {sisa_kursi}")

    try:
        umur = int(input("Masukkan umur penumpang: "))
    except ValueError:
        print("Input umur harus berupa angka!")
        continue

    if umur < 0:
        print("Umur tidak valid!")
        continue

    if umur <= 5:
        harga = 0
        print(f"Kategori: Balita - Tiket Gratis (Rp {harga})")
    elif umur <= 12:
        harga = 50000
        print(f"Kategori: Anak - Harga: Rp {harga}")
    else:
        harga = 100000
        print(f"Kategori: Dewasa - Harga: Rp {harga}")

    total_pendapatan += harga
    sisa_kursi -= 1

print("\n--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")