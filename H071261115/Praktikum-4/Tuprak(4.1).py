def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal *= 0.9
    return subtotal
 
 
print("Selamat datang di Kasir Minimarket!")
 
total_belanja = 0
 
while True:
    status_member = input("Apakah Anda member (Y?N): ")
    if status_member == "":
        is_member = True
    else:
        print ("Inputan hanya bisa 'Y' atau 'N'")
        continue

    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ").strip
    if nama_barang == "":
        break
 
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
 
    subtotal = hitung_subtotal(harga, jumlah, is_member)
    print(f"Subtotal {nama_barang}: Rp{int(subtotal)}")
 
    total_belanja += subtotal
 
print(f"Total belanja: Rp{int(total_belanja)}")
 