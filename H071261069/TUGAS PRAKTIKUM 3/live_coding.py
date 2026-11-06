while True:
    jumlah_barang = int(input('Masukkan jumlah barang : '))
    total_belanja = 0
    if jumlah_barang <= 0:
        print('Input tidak valid')
        continue

    for i in range(1, jumlah_barang + 1):
        print(f"Barang ke-{i}")
        nama = input("Nama   : ")
        harga = float(input("Harga  : "))
        jumlah = float(input("Jumlah :"))
       
        if harga < 0 or jumlah < 0:
            print("Input tidak valid!")
            continue
        else:
            subtotal = harga * jumlah
            total_belanja += subtotal

    print(f"\nTotal belanja: Rp{total_belanja}")

    if total_belanja >= 500000:
        print("Mendapatkan diskon")
    else:
        print("Tidak mendapatkan diskon")
    break