# Soal 3 - Sistem Reservasi PO BUS

# Input kursi bus (validasi angka dan harus > 0)
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

print()
print("--- Sistem Reservasi PO BUS Dimulai ---")

pendapatan = 0

while sisa_kursi > 0:
    print()
    print(f"Sisa kursi: {sisa_kursi}")

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
        print("Kategori: Balita - Tiket Gratis (Rp 0)")
    elif umur <= 12:
        harga = 50000
        print("Kategori: Anak - Harga: Rp 50.000")
    else:
        harga = 100000
        print("Kategori: Dewasa - Harga: Rp 100.000")

    sisa_kursi -= 1
    pendapatan += harga

print()
print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {pendapatan}")