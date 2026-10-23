#Subtotal harga barang
def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = subtotal * 0.9  #Ada discount 10%
    return subtotal

#Processing program
def main():
    print("Selamat datang di Kasir Minimarket!")
    status = input("Apakah Anda member? (y/n): ").strip().lower()
    adalah_member = (status == "y") #Status member

    total = 0

    while True: #Input barang
        nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
        if nama_barang == "":
            break #Menghentikan proses input

        harga = int(input("Harga barang: "))
        jumlah = int(input("Jumlah barang: "))

        subtotal = hitung_subtotal(harga, jumlah, adalah_member)
        total += subtotal
        print(f"Subtotal {nama_barang}: Rp{int(subtotal)}")

    print(f"Total belanja: Rp{int(total)}")

main()