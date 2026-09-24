print ("=== SETUP DENAH BIOSKOP NONTONYUK ===\n")

while True:
    try:
        jumlah_baris = int(input("Masukkan jumlah baris: "))
        if jumlah_baris <= 0:
            print ("Jumlah baris harus lebih dari 0!")
            continue
        break
    except:
        print ("Input baris harus berupa angka!")

while True: 
    try: 
        jumlah_kursi = int(input("Masukkan jumlah kursi dalam satu baris: "))
        if jumlah_kursi <= 0:
            print ("Jumlah kursi harus lebih dari 0!")
            continue
        break
    except:
        print ("Input kursi harus berupa angka!")

print ("\n=== Daftar Kursi Tersedia ===\n")

for baris in range (1, jumlah_baris+1):
    for kursi in range (1, jumlah_kursi+1):
        if kursi == 13:
            continue
        if baris == 1 and kursi % 2 == 0:
            continue
        print (f"Baris {baris} - Kursi {kursi}")
    print ()