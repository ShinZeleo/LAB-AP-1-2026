def hitung_subtotal(harga, jumlah, adalah_member = False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal *= 0.9
    return subtotal

print("=== Selamat datang di Kasir Minimarket! ===")

while True:
    status_member = input("Apakah Anda member? (Y/N): ").strip().upper()
    if status_member in ['Y', 'N']:
        break
    print ("Input salah! Hanya bisa 'Y' atau 'N'.")
adalah_member = (status_member == "Y")

total_belanja = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ").strip()
    if nama_barang == "":         
        break

    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, adalah_member)
    print(f"Subtotal {nama_barang}: Rp{subtotal}")
    total_belanja += subtotal

print(f"Total belanja: Rp{total_belanja}")