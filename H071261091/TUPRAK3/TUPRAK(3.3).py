while True:
    try:
        jumlah_kursi = int((input("Masukkan Jumlah Maksimal Kursi Bus: ")))
        if jumlah_kursi < 0:
            print ("Input salah!Jumlah tidak boleh negatif.")
            continue
        break
    except:
        print ("Input jumlah kursi harus berupa angka!")

pendapatan = 0

print ("\n=== SISTEM RESERVASI PO BUS Dimulai ===")

while jumlah_kursi > 0:
    try:
        umur = int(input("Masukkan Umur Penumpang: "))
        if umur < 0:
            print ("Umur tidak valid!")
            print (f"Sisa kursi: {jumlah_kursi}")
            continue
        if umur <= 5:
            print ("Kategori: Balita - Tiket Gratis (Rp 0)")
            harga = 0
        elif umur <= 12:
            print ("Kategori: Anak - Harga: Rp 50.000")
            harga = 50000
        else:
            print ("Kategori: Dewasa - Harga: Rp 100.000")
            harga = 100000
        jumlah_kursi -= 1
        print (f"Sisa kursi: {jumlah_kursi}\n")
        pendapatan += harga
    except:
        print ("Input umur harus berupa angka!")
print ("\n=== Semua Kursi Terisi! ===")
print("Total pendapatan: Rp", pendapatan)