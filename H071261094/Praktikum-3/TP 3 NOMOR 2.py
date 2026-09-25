print("--- Setup Denah Bioskop NontonYuk ---")

# jumlah baris
while True:
    try:
        jumlah_baris = int(input("Masukkan jumlah baris: "))
    except ValueError:
        print("Input baris harus berupa angka!\n")
        continue
    
    if jumlah_baris <= 0:
        print("Jumlah baris harus lebih dari 0!\n")
        continue
    break

# jumlah kursi per baris
while True:
    try:
        jumlah_kursi = int(input("Masukkan jumlah kursi per baris: "))
    except ValueError:
        print("Input kursi harus berupa angka!\n")
        continue
    
    if jumlah_kursi <= 0:
        print("Jumlah kursi harus lebih dari 0!\n")
        continue
    break

print("\n--- Daftar Kursi Tersedia ---")

# Nested loop: baris luar, kursi dalam
for baris in range(1, jumlah_baris + 1):
    for kursi in range(1, jumlah_kursi + 1):
        
        if kursi == 13:
            continue  # aturan mitos, lewati kursi 13
        
        if baris == 1 and kursi % 2 == 0:
            continue  # baris VVIP hanya kursi ganjil
        
        print(f"Baris {baris} - Kursi {kursi}")