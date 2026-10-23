import os
import random
from datetime import datetime 

FOLDER = "invoices"
FILE_RIWAYAT = "trx_history.txt"

#trx_history.txt
LEBAR_WAKTU = 19
LEBAR_ID = 17
LEBAR_NOMINAL = 18

def input_teks(pesan):
    while True:
        nilai = input(pesan).strip().title()
        if nilai:
            return nilai
        print("  Input tidak boleh kosong, coba lagi.")

def format_rupiah(nominal):
    return "Rp. " + str(nominal)

def path_invoice(id_transaksi):
    return os.path.join(FOLDER, id_transaksi + ".txt")

# NOMOR 1
def buat_inisial(nama_kasir):
    return "".join(kata[0] for kata in nama_kasir.split()).upper()


def buat_id_transaksi(nama_kasir, waktu):
    inisial = buat_inisial(nama_kasir)
    bagian_waktu = waktu.strftime("%y%m%d%H%M")
    while True:
        acak = random.randint(100, 999)
        id_transaksi = inisial + bagian_waktu + str(acak)
        if not os.path.exists(path_invoice(id_transaksi)):
            return id_transaksi


def input_produk():
    produk_list = []
    while True:
        nama_produk = input("Masukkan nama produk : ").title()
        harga_produk = int(input("Masukkan harga produk : "))
        jumlah_produk = int(input("Masukkan jumlah produk : "))
        produk_list.append({"nama": nama_produk, "harga": harga_produk, "jumlah": jumlah_produk})
        print(40*"=")
        opsi_tambah = input("Tambah produk? (y/t): ").strip().lower()
        print(40*"=")
        if opsi_tambah != "y":
            return produk_list

def susun_invoice(id_transaksi, waktu, nama_kasir, daftar_produk, total):
    garis_ganda = "=" * 58
    garis_tunggal = "-" * 58
    baris = [
        garis_ganda,
        "INVOICE BELANJA".center(58),
        garis_ganda,
        "ID Transaksi : " + id_transaksi,
        "Waktu        : " + waktu.strftime("%Y-%m-%d %H:%M:%S"),
        "Kasir        : " + nama_kasir,
        garis_tunggal,
        f"{'No':<4}{'Produk':<20}{'Harga':>10}{'Qty':>6}{'Subtotal':>16}",
        garis_tunggal,
    ]
    for i, p in enumerate(daftar_produk, start=1):
        subtotal = p["harga"] * p["jumlah"]
        baris.append(
            f"{i:<4}{p['nama'][:19]:<20}{p['harga']:>10}{p['jumlah']:>6}{subtotal:>16}"
        )
    baris += [
        garis_tunggal,
        f"{'TOTAL':<40}{format_rupiah(total):>18}",
        garis_ganda,
        "Terima kasih telah berbelanja!".center(58),
        garis_ganda,
    ]
    return "\n".join(baris) + "\n"

def simpan_invoice(id_transaksi, isi_invoice):
    try:
        os.makedirs(FOLDER, exist_ok=True)
        with open(path_invoice(id_transaksi), "w", encoding="utf-8") as f:
            f.write(isi_invoice)
        return True
    except IOError:
        print("Error: tidak bisa menyimpan invoice " + id_transaksi)
        return False

def transaksi_baru():
    daftar_produk = input_produk()
    waktu = datetime.now()
    total = sum(p["harga"] * p["jumlah"] for p in daftar_produk)
    id_transaksi = buat_id_transaksi(nama_kasir, waktu)
    isi_invoice = susun_invoice(id_transaksi, waktu, nama_kasir, daftar_produk, total)
    if not simpan_invoice(id_transaksi, isi_invoice):
        print("Transaksi dibatalkan karena invoice gagal disimpan.")
        return
 
    catat_riwayat(waktu, id_transaksi, total)

    print(10*' '+"TRANSAKSI BERHASIL")

# NOMOR 2
def baca_invoice(id_transaksi):
    try:
        with open(path_invoice(id_transaksi), "r", encoding="utf-8") as f:
            data = f.read()
            print()
            print(data)
    except FileNotFoundError:
        print("Invoice dengan ID " + id_transaksi + " tidak ditemukan.")
    except IOError:
        print("Error: tidak bisa membaca invoice " + id_transaksi)
 
def cari_invoice():
    print("\n===== CARI INVOICE =====")
    id_transaksi = input("Masukkan ID transaksi: ")
 
    
    if not id_transaksi.isalnum():
        print("ID transaksi tidak valid (hanya huruf dan angka, tanpa spasi).")
        return
 
    baca_invoice(id_transaksi)

# NOMOR 3
def garis_tabel():
    return "=" * (LEBAR_WAKTU + LEBAR_ID + LEBAR_NOMINAL + 10)
 
 
def baris_tabel(waktu, id_transaksi, nominal, rata_tengah=False):
    if rata_tengah:
        w = waktu.center(LEBAR_WAKTU)
        i = id_transaksi.center(LEBAR_ID)
        n = nominal.center(LEBAR_NOMINAL)
    else:
        w = waktu.ljust(LEBAR_WAKTU)
        i = id_transaksi.ljust(LEBAR_ID)
        n = nominal.ljust(LEBAR_NOMINAL)
    return "| " + w + " | " + i + " | " + n + " |"

def catat_riwayat(waktu, id_transaksi, total):
    perlu_header = (not os.path.exists(FILE_RIWAYAT)) or os.path.getsize(FILE_RIWAYAT) == 0
    try:
        with open(FILE_RIWAYAT, "a", encoding="utf-8") as f:
            if perlu_header:
                f.write(garis_tabel() + "\n")
                f.write(baris_tabel("Waktu", "ID Transaksi", "Nominal Transaksi", True) + "\n")
                f.write(garis_tabel() + "\n")
            f.write(
                baris_tabel(
                    waktu.strftime("%Y-%m-%d %H:%M:%S"),
                    id_transaksi,
                    format_rupiah(total),
                )
                + "\n"
            )
            f.write(garis_tabel() + "\n")
    except IOError:
        print("Error: tidak bisa menulis ke file " + FILE_RIWAYAT)

# OUTPUT    
print(40*"=")
print(10*' '+"SELAMAT DATANG")
print(40*"=")
nama_kasir = input_teks("Masukkan nama kasir: ")
while True:
    print(40*"=")
    print('Pilih opsi:')
    print('1. Transaksi baru')
    print('2. Cari transaksi')
    print('3. Keluar')
    print(40*"=")
    
    pilihan = int(input("Masukkan opsi pilihan : "))
    print(40*"=")
    if pilihan == 1:
        transaksi_baru()
    if pilihan == 2:
        cari_invoice()
    if pilihan == 3:
        print(10*" ","SAMPAI JUMPA")
        print(40*"=")
        break