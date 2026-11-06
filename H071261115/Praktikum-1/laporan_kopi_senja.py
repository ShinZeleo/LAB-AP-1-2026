menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# 1. Subtotal masing-masing menu
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

# 2. Masukkan ketiga subtotal ke dalam list
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# 3. Total pendapatan & pendapatan bersih
BIAYA_OPERASIONAL = 15000
total_seluruh = sum(subtotal_pendapatan)
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

# 4. Jumlah barang terjual & target tercapai
jumlah_barang_terjual = jumlah[0]+jumlah[1]+jumlah[2]
target_tercapai = total_seluruh > 200000 and jumlah_barang_terjual > 10

# Tampilkan hasil
print("=== Laporan Penjualan Kopi Senja ===")
print("Subtotal Kopi Susu      : ", sub_kopi)
print("Subtotal Matcha Latte   : ", sub_matcha)
print("Subtotal Americano      : ", sub_americano)
print("List subtotal_pendapatan: ", subtotal_pendapatan)
print("Total Pendapatan        : ", total_seluruh)
print("Biaya Operasional       : ", BIAYA_OPERASIONAL)
print("Pendapatan Bersih       : ", pendapatan_bersih)
print("Jumlah Barang Terjual   : ", jumlah_barang_terjual)
print("Target Tercapai         : ", target_tercapai)
