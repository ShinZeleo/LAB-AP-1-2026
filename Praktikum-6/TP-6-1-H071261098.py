def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku_baru = {"judul": judul, "penulis": penulis,"harga": harga, "stok": stok}
    inventaris.append(buku_baru)
    print(f"Buku '{judul}' berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)

    if len(hasil) == 0:
        print(f"Buku dengan kata kunci '{kata_kunci}' tidak ditemukan.")
    else:
        print(f"Ditemukan {len(hasil)} buku:")
        nomor = 1
        for buku in hasil:
            print(f" {nomor}. {buku['judul']} - {buku['penulis']} | Rp{buku['harga']} | Stok: {buku['stok']}")
            nomor = nomor + 1


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0:
                print(f"Gagal! Stok tidak mencukupi. Stok saat ini: {buku['stok']}")
            else:
                buku["stok"] = stok_baru
                if jumlah > 0:
                    print(f"Stok '{buku['judul']}' bertambah {jumlah}. Stok sekarang: {buku['stok']}")
                elif jumlah < 0:
                    print(f"Stok '{buku['judul']}' berkurang {-jumlah}. Stok sekarang: {buku['stok']}")
                else:
                    print("Jumlah perubahan 0, stok tidak berubah.")
            return
    print(f"Error: Buku '{judul}' tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)
    if len(inventaris) == 0:
        print("Inventaris masih kosong.")
        print("=" * 40)
        return

    total_stok = 0
    total_aset = 0
    termahal = inventaris[0]
    for buku in inventaris:
        total_stok = total_stok + buku["stok"]
        total_aset = total_aset + buku["harga"] * buku["stok"]
        if buku["harga"] > termahal["harga"]:
            termahal = buku

    print(f"Jumlah jenis buku : {len(inventaris)}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset}")
    print(f"Buku termahal     : {termahal['judul']} (Rp{termahal['harga']})")
    print("=" * 40)


inventaris = []

print("=" * 40)
print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("=" * 40)

while True:
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ").strip()

    if pilihan == "1":
        judul = input("Judul buku: ").strip()
        penulis = input("Penulis: ").strip()
        if judul == "" or penulis == "":
            print("Judul dan penulis tidak boleh kosong.")
        else:
            try:
                harga = int(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Harga dan stok tidak boleh negatif.")
                else:
                    tambah_buku(inventaris, judul, penulis, harga, stok)
            except ValueError:
                print("Harga dan stok harus berupa angka bulat.")

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ").strip()
        if kata_kunci == "":
            print("Kata kunci tidak boleh kosong.")
        else:
            cari_buku(inventaris, kata_kunci)

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ").strip()
        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris, judul, jumlah)
        except ValueError:
            print("Jumlah perubahan harus berupa angka bulat.")

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak valid, masukkan angka 1-5.")