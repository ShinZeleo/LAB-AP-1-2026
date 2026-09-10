# Laporan Penjualan "Kopi Senja"
menu = ['Kopi Susu', 'Matcha Latte', 'Americano']
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# 1. menentukan subtotal
sub_kopi = jumlah[0]*harga[0]
sub_matcha = jumlah[1]*harga[1]
sub_americano = jumlah[2]*harga[2]

# 2. memasukkan dalam list sub total pendapatan
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# 3. menentukan pendapatan bersih
total_seluruh = (sub_kopi + sub_matcha + sub_americano)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

# 4. jumlah barang dan target yang tercapai
jumlah_barang = (jumlah[0] + jumlah[1] + jumlah[2])
target_tercapai = pendapatan_bersih > 200000 and jumlah_barang > 10

# 5. output Laporan Penjualan "Kopi Senja"
print("=== LAPORAN PENJUALAN KOPI SENJA ===")
print(f"Subtotal Kopi Susu : Rp{sub_kopi}")
print(f"Subtotal Matcha Latte : Rp{sub_matcha}")
print(f"Subtotal Americano : Rp{sub_americano}")

print(f"\nTotal Seluruh : Rp{total_seluruh}")
print(f"Biaya Operasional : Rp{BIAYA_OPERASIONAL}")
print(f"Pendapatan Bersih : Rp{pendapatan_bersih}")
print(f"\nJumlah Barang Terjual : {jumlah_barang}")
print(f"Hasil Target : {target_tercapai}")



