print("Setup Denah Bioskop NontonYuk")


while True:
    try:
        baris = int(input("Masukkan jumlah baris: "))
        if baris <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input baris harus berupa angka!")


while True:
    try:
        kursi_per_baris = int(input("Masukkan jumlah kursi per baris: "))
        if kursi_per_baris <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input kursi harus berupa angka!")

print("Daftar Kursi Tersedia")


for b in range(1, baris + 1):
    for k in range(1, kursi_per_baris + 1):
        
        if k == 13:
            continue
        
        
        if b == 1:
            if k % 2 != 0:
                print(f"Baris {b} Kursi {k}")
        
        else:
            print(f"Baris {b} Kursi {k}")