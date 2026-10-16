print("--- Rekapitulasi Transaksi Dins Store ---")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.\n")

while True:

    
    try:
        jumlah_item = int(input("Masukkan jumlah item: "))
    except ValueError:
        print("Input harus berupa angka!\n")
        continue  # kembali ke awal loop, minta input lagi
    
    if jumlah_item == 0:
        print("Toko ditutup. Sesi rekap selesai.")
        break  # keluar total dari loop
    
    if jumlah_item < 0:
        print("Jumlah tidak boleh negatif\n")
        continue
    
    if jumlah_item > 100:
        print("Maksimal 100 item per transaksi!\n")
        continue
    
    print(f"Transaksi {jumlah_item} item berhasil!\n")