def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = subtotal * 90 // 100 
    return subtotal

print("selamat datang di kasir minimarket!")
status = input("apakah anda member? (y/n):")
member = status.lower() == "y"
total = 0

while True:
    nama = input("nama barang (kosongan untuk selesai): ")
    if nama == "":
        break
    harga = int(input("harga barang: "))
    jumlah = int(input("jumlah  barang: "))

    subtotal = hitung_subtotal(harga, jumlah, member)
    print(f"subtotal {nama}: Rp{subtotal}")
    total += subtotal

print(f"total belanja: Rp{total}")
