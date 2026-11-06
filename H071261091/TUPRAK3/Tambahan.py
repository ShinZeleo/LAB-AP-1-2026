total_harga = int(input("Masukkan Total Harga: "))
jumlah_uang = int(input("Jumlah Uang Pelanggan: "))

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

kembalian = jumlah_uang - total_harga

for pecahan in pecahan_uang:
    jumlah_lembar = kembalian // pecahan
    if jumlah_lembar > 0:
        print (f"{jumlah_lembar} lembar pecahan Rp {pecahan}")
        kembalian = kembalian % pecahan