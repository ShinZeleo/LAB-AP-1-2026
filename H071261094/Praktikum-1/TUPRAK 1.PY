# Data Penjualan
menu = ["Kopi Susu", "Matcha Latte", "Americanoo"]
harga = [18000, 22000, 15000,]
jumlah = [4, 3, 5]

# Menghitung subtotal setiap minuman
sub_Kopi = harga[0] * jumlah[0]
sub_Matcha = harga[1] * jumlah[1]
sub_Americano = harga[2] * jumlah[2]

# Menghitung total pendapatan
subtotal_pendapatan = [sub_Kopi, sub_Matcha, sub_Americano]
total_pendapatan = sub_Kopi + sub_Matcha + sub_Americano

# Menghitung pendapatan setelah dikurangi biaya operasional
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_pendapatan - BIAYA_OPERASIONAL

# Menghitung total jumlah barang yang terjual
total_barang = jumlah [0] + jumlah [1] + jumlah [2]
target_tercapai = total_pendapatan > 200000 and total_barang > 10

# Hasil 
print("Total Kopi Susu yang terjual: Rp", sub_Kopi)
print("Total Matcha Latte yang terjual: Rp", sub_Matcha)
print("Total Americano yang terjual: Rp", sub_Americano)
print("Pendapatan Bersih:", pendapatan_bersih)
print("Subtotal Pendapatan:", total_pendapatan)
print("Target Tercapai:", target_tercapai)







