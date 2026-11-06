print("--- Rekapitulasi Transaksi Dins Store ---")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.\n")
while True:
    try:
        jumlah = int(input(f"Masukkan jumlah item:"))
    except ValueError:
        print("Input harus berupa angka!\n")
        continue

    if jumlah < 0:
        print("Jumlah tidak boleh negatif\n")
        continue
    
    if jumlah > 100:
        print("Maksimal 100 item per transaksi\n")
        continue

    if jumlah == 0:
        print("Toko ditutup. Sesi rekap selesai.")
        break

    print(f"Transaksi {jumlah} item berhasil!\n")

