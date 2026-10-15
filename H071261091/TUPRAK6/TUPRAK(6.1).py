def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {"judul": judul, "penulis": penulis, "harga": harga, "stok": stok}
    inventaris.append(buku)
    print (f"Buku '{judul}' berhasil ditambahkan!")

def cari_buku(inventaris, kata_kunci):
    hasil_pencarian = []
    for buku in inventaris:
        if kata_kunci in buku["judul"].lower():
            hasil_pencarian.append(buku)
    if len(hasil_pencarian) > 0:
        print (f"Ditemukan {len(hasil_pencarian)} buku:")
        nomor = 1
        for b in hasil_pencarian:
            print (f"{nomor}. {b['judul']} - {b['penulis']} | Rp{b['harga']} | Stok: {b['stok']}")
            nomor += 1
    else:
        print ("Tidak ada buku yang cocok dengan kata kunci.")

def update_stok(inventaris, update, perubahan_stok):
    ditemukan = False
    for buku in inventaris:
        if buku["judul"] == update:
            ditemukan = True
            stok_baru = buku["stok"] + perubahan_stok
            if stok_baru < 0:
                print ("Gagal! Stok menjadi negatif setelah perubahan.")
            else:
                buku["stok"] = stok_baru
                if perubahan_stok >= 0:
                    print (f"Stok {buku['judul']} bertambah {perubahan_stok}. Stok sekarang: {buku['stok']}")
                else:
                    print (f"Stok {buku['judul']} berkurang {-perubahan_stok}. Stok sekarang: {buku['stok']}")
            break
    if not ditemukan:
        print ("Error: Buku tidak ditemukan dalam inventaris.")

def ringkasan_inventaris(inventaris):
    print ("\n=======================================")
    print ("     RINGKASAN INVENTARIS BOOKNEST     ")
    print ("=======================================\n")
    
    if len(inventaris) == 0:
        return "Inventaris masih kosong."

    jumlah_jenis = len(inventaris)
    total_stok = 0
    total_aset = 0
    termahal = inventaris[0]

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += (buku["harga"]*buku["stok"])
        if buku["harga"] > termahal["harga"]:
            termahal = buku

    print ("Jumlah jenis buku   : ", jumlah_jenis)
    print ("Total seluruh stok  : ", total_stok)
    print ("Total nilai aset    : Rp", total_aset)
    print (f"Buku termahal       : {termahal['judul']} (Rp{termahal['harga']})")
    print ("=======================================")

inventaris_buku = []

while True:
    print ("\n========================================")
    print ("  SISTEM INVENTARIS TOKO BUKU BOOKNEST  ")
    print ("========================================\n")

    print ("Menu: ")
    print ("1. Tambah Buku")
    print ("2. Cari Buku")
    print ("3. Update Stok")
    print ("4. Ringkasan Inventaris")
    print ("5. Keluar")

    menu = input("Pilih menu (1-5): ")
    if menu == "1":
        judul = input("Judul buku: ").title()
        penulis = input("Penulis: ").title()
        try:
            harga = int(input("Harga (Rp): "))
            stok = int(input("Stok awal: "))
            if harga < 0 or stok < 0:
                print ("Error: Harga dan Stok tidak boleh negatif!")
                continue
            else:
                tambah_buku(inventaris_buku, judul, penulis, harga, stok)
        except ValueError:
            print ("Error: Harga dan Stok hanya boleh berupa angka!")

    elif menu == "2":
        kata_kunci = input("Masukkan kata kunci judul: ").lower()
        cari_buku(inventaris_buku, kata_kunci)

    elif menu == "3":
        update = input ("Judul buku yang ingin diupdate: ").title()
        perubahan_stok = int(input("Jumlah perubahan (positif = tambah, negatif = kurang): "))
        update_stok(inventaris_buku, update, perubahan_stok)

    elif menu == "4":
        ringkasan_inventaris(inventaris_buku)

    elif menu == "5":
        print ("Terima kasih telah menggunakan BookNest!")
        break