def tambah_buku(inventaris, judul, penulis, harga, stok):
    """Menambahkan satu buku (dictionary) ke dalam list inventaris."""
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok,
    }
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    """Mencari buku berdasarkan kata kunci pada judul (tidak peka huruf besar/kecil)."""
    hasil = [
        buku for buku in inventaris
        if kata_kunci.lower() in buku["judul"].lower()
    ]

    if not hasil:
        print("Buku tidak ditemukan.")
        return

    print(f"Ditemukan {len(hasil)} buku:")
    for i, buku in enumerate(hasil, start=1):
        print(f"  {i}. {buku['judul']} - {buku['penulis']} | "
              f"Rp{buku['harga']} | Stok: {buku['stok']}")


def update_stok(inventaris, judul, jumlah):
    """Mengubah stok buku. Jumlah positif = tambah, negatif = kurang."""
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print(f"Gagal! Stok '{buku['judul']}' tidak mencukupi. "
                      f"Stok saat ini: {buku['stok']}")
                return

            buku["stok"] = stok_baru
            if jumlah >= 0:
                print(f"Stok '{buku['judul']}' bertambah {jumlah}. "
                      f"Stok sekarang: {buku['stok']}")
            else:
                print(f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. "
                      f"Stok sekarang: {buku['stok']}")
            return

    print(f"Error! Buku '{judul}' tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    """Menampilkan ringkasan inventaris."""
    garis = "=" * 40
    print(garis)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print(garis)

    if not inventaris:
        print("Inventaris masih kosong.")
        print(garis)
        return

    jumlah_jenis = len(inventaris)
    total_stok = sum(buku["stok"] for buku in inventaris)
    total_aset = sum(buku["harga"] * buku["stok"] for buku in inventaris)
    termahal = max(inventaris, key=lambda buku: buku["harga"])

    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset}")
    print(f"Buku termahal     : {termahal['judul']} (Rp{termahal['harga']})")
    print(garis)


def main():
    inventaris = []
    garis = "=" * 40

    print(garis)
    print("  SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print(garis)

    while True:
        print()
        print("Menu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            judul = input("Judul buku: ")
            penulis = input("Penulis: ")
            try:
                harga = int(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Error! Harga dan stok tidak boleh negatif.")
                else:
                    tambah_buku(inventaris, judul, penulis, harga, stok)
            except ValueError:
                print("Error! Harga dan stok harus berupa angka.")

        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris, kata_kunci)

        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ")
            try:
                jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
                update_stok(inventaris, judul, jumlah)
            except ValueError:
                print("Error! Jumlah perubahan harus berupa angka.")

        elif pilihan == "4":
            ringkasan_inventaris(inventaris)

        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break

        else:
            print("Pilihan tidak valid. Masukkan angka 1-5.")


if __name__ == "__main__":
    main()