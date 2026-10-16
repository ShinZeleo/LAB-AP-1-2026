# Soal 2 - Denah Kursi Bioskop
print("--- Setup Denah Bioskop NontonYuk ---")

# Input jumlah baris (validasi angka dan harus > 0)
while True:
    try:
        jumlah_baris = int(input("Masukkan jumlah baris: "))
    except ValueError:
        print("Input baris harus berupa angka!")
        print()
        continue

    if jumlah_baris <= 0:
        print("Jumlah baris harus lebih dari 0!")
        print()
        continue

    break

# Input jumlah kursi per baris (validasi angka dan harus > 0)
while True:
    try:
        jumlah_kursi = int(input("Masukkan jumlah kursi per baris: "))
    except ValueError:
        print("Input kursi harus berupa angka!")
        print()
        continue

    if jumlah_kursi <= 0:
        print("Jumlah kursi harus lebih dari 0!")
        print()
        continue

    break

print()
print("--- Daftar Kursi Tersedia ---")

# Nested loop: loop luar = baris, loop dalam = kursi
for baris in range(1, jumlah_baris + 1):
    for kursi in range(1, jumlah_kursi + 1):
        # Aturan Mitos: kursi 13 tidak dijual di baris mana pun
        if kursi == 13:
            continue
        # Aturan VVIP: baris 1 hanya kursi ganjil
        if baris == 1 and kursi % 2 == 0:
            continue
        print(f"Baris {baris} - Kursi {kursi}")