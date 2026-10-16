#PROCESSING PROGRAM
#Program Untuk Menambah Buku
def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {"judul": judul, "penulis": penulis, "harga": harga, "stok": stok}
    inventaris.append(buku) #menambahkan ke inventaris
    print(f"Buku '{judul}' berhasil ditambahkan!")

#Program Untuk Mencari Buku
def cari_buku(inventaris, kata_kunci):
    kata_kunci = kata_kunci.lower()
    hasil = [b for b in inventaris if kata_kunci in b["judul"].lower()] #b mewakili kata kunci(judul buku)
    if hasil:
        print(f"Ditemukan {len(hasil)} buku:") #menjumlahkan hasil pencarian
        for i, b in enumerate(hasil, 1): #melacak hasil pencarian
            print(f" {i}. {b['judul']} - {b['penulis']} | Rp{b['harga']} | Stok: {b['stok']}") #print hasil pencarian
    else:
        print("Buku tidak ditemukan.")
    return hasil

#Program Untuk Mengupdate Stok
def update_stok(inventaris, judul, jumlah):
    for b in inventaris:
        if b["judul"].lower() == judul.lower():
            stok_baru = b["stok"] + jumlah #menambah atau mengurangi stok
            if stok_baru < 0: #jika stok baru kurang dari 0, stok tidak mencukupi
                print(f"Gagal! Stok '{b['judul']}' tidak mencukupi (stok saat ini: {b['stok']}).")
                return False
            b["stok"] = stok_baru
            if jumlah >= 0: #jika parameter jumlah lebih besar dari 0, stok bertambah
                print(f"Stok '{b['judul']}' bertambah {jumlah}. Stok sekarang: {b['stok']}")
            else: #jika parameter jumlah kurang dari 0, stok berkurang
                print(f"Stok '{b['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {b['stok']}")
            return True
    print(f"Error: Buku '{judul}' tidak ditemukan.")
    return False

#Program Untuk Menampilkan Ringkasan Inventaris
def ringkasan_inventaris(inventaris):
    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)
    if not inventaris:
        print("Inventaris masih kosong.")
        print("=" * 40)
        return
    jumlah_jenis = len(inventaris) #menghitung jumlah jenis buku
    total_stok = sum(b["stok"] for b in inventaris) #menghitung total stok
    total_aset = sum(b["harga"] * b["stok"] for b in inventaris) #menghitung total aset(harga * stok)
    termahal = max(inventaris, key=lambda b: b["harga"]) #mencari buku dengan harga tertinggi
    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{total_aset}")
    print(f"Buku termahal : {termahal['judul']} (Rp{termahal['harga']})")
    print("=" * 40)

#INPUT DAN OUTPUT PROGRAM
#Program Untuk Menampilkan Menu
def tampilkan_menu():
    print("Menu:") 
    print("1. Tambah Buku") 
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

#Program Utama
def main():
    inventaris = []
    print("=" * 40)
    print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("=" * 40)

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            judul = input("Judul buku: ")
            penulis = input("Penulis: ")
            try: 
                harga = int(input("Harga: ")) 
                stok = int(input("Stok awal: "))
            except ValueError:
                print("Error: Harga dan stok harus berupa angka!")
                continue
            if harga < 0 or stok < 0:
                print("Error: Harga dan stok tidak boleh negatif!")
                continue
            tambah_buku(inventaris, judul, penulis, harga, stok) #program untuk menambah buku

        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris, kata_kunci) #program untuk mencari buku

        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ")
            try:
                jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            except ValueError:
                print("Error: Jumlah harus berupa angka!")
                continue
            update_stok(inventaris, judul, jumlah) #program untuk mengupdate stok

        elif pilihan == "4":
            ringkasan_inventaris(inventaris) #program untuk menampilkan ringkasan inventaris

        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break

        else:
            print("Pilihan tidak valid. Masukkan angka 1-5.")

main()