def hitung_subtotal(harga, jumlah, adalah_member=False):
    """Menghitung subtotal satu jenis barang, diskon 10% jika member."""
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = subtotal * 90 // 100  
    return subtotal

def main():
    while True: 
        print("Selamat datang di Kasir Minimarket!")
        status_member = input("Apakah Anda member? (y/n): ").strip().lower()
        if status_member in ["y", "n"]:
            break
        print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")

    adalah_member = (status_member == "y")
        

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

main()