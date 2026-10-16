menu = ["kopi_susu", "matcha_latte", "americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi_susu = harga[0] * jumlah[0]
sub_matcha_latte = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

subtotal_pendapatan = [sub_kopi_susu, sub_matcha_latte, sub_americano]

total_seluruh = sum(subtotal_pendapatan)
biaya_operasional = 15000
pendapatan_bersih = total_seluruh - biaya_operasional

jumlah_barang = jumlah[0] + jumlah [1] + jumlah [2]
target_tercapai = total_seluruh > 200000 and jumlah_barang > 10 

print(f"subtotal kopi susu : Rp{sub_kopi_susu}")
print(f"subtotal matcha latte :Rp{sub_matcha_latte}")
print(f"subtotal americano : Rp{sub_americano}")
print(f"total seluruh : Rp{total_seluruh}")
print(f"pendapatan bersih : Rp{pendapatan_bersih}")
print(f"total barang terjual : {jumlah_barang} pcs")   
print(f"target tercapai : {target_tercapai}")     


