import os
import random
from datetime import datetime

FOLDER_INVOICE = "invoices"
FILE_RIWAYAT = "trx_history.txt"
GARIS_RIWAYAT = "=" * 66


def rupiah(angka):
    return f"Rp. {angka}"

def ambil_inisial(nama):
    kata = nama.split()
    if len(kata) > 1:
        return "".join(k[0] for k in kata).upper() #huruf pertama tiap kata (Kasir Lima Sejahtera -> KLS)
    return nama[:3].upper() #3 huruf pertama (Kelvin -> KEL)

def buat_id_transaksi(nama_kasir, waktu):
    inisial = ambil_inisial(nama_kasir)
    bagian_waktu = waktu.strftime("%y%m%d%H%M") #string format time
    while True:
        acak = random.randint(100, 999) # random integer, 3 digit acak
        id_trx = f"{inisial}{bagian_waktu}{acak}" #format
        if not os.path.exists(os.path.join(FOLDER_INVOICE, id_trx + ".txt")): #memastikan ID belum pernah dipakai
            return id_trx

def input_angka(pesan, minimum=1):
    while True: #validasi angka
        teks = input(pesan).strip()
        try:
            nilai = int(teks)
        except ValueError:
            print("  ! Masukkan angka bulat yang valid.")
            continue
        if nilai < minimum:
            print(f"  ! Nilai minimal {minimum}.")
            continue
        return nilai

def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks:
            return teks
        print("  ! Tidak boleh kosong.")

#MAKING INVOICE 
def susun_invoice(id_trx, waktu, kasir, items, total):
    lebar = 62
    baris = []
    baris.append("=" * lebar)
    baris.append("INVOICE".center(lebar))
    baris.append("=" * lebar)
    baris.append(f"ID Transaksi : {id_trx}")
    baris.append(f"Waktu        : {waktu.strftime('%Y-%m-%d %H:%M:%S')}")
    baris.append(f"Kasir        : {kasir}")
    baris.append("-" * lebar)
    baris.append(f"{'No':<4}{'Produk':<20}{'Harga':>10}{'Qty':>6}{'Subtotal':>16}") #design tampilan
    baris.append("-" * lebar)
    for no, (nama, harga, qty) in enumerate(items, start=1): #hitung dan urutkan item
        baris.append(f"{no:<4}{nama[:19]:<20}{harga:>10}{qty:>6}{harga * qty:>16}")
    baris.append("-" * lebar)
    baris.append(f"{'TOTAL':<40}{rupiah(total):>22}")
    baris.append("=" * lebar)
    baris.append("Terima kasih telah berbelanja!".center(lebar))
    baris.append("=" * lebar)
    return "\n".join(baris) + "\n" #mengurutkan

def simpan_invoice(id_trx, isi):
    os.makedirs(FOLDER_INVOICE, exist_ok=True) #folder
    path = os.path.join(FOLDER_INVOICE, id_trx + ".txt")
    with open(path, "w", encoding="utf-8") as f: #encoding menerjemahkan dan menyimpan simbol khusus
        f.write(isi)
    return path

#TRANSACTION HISTORY
def catat_riwayat(waktu, id_trx, total):
    baru = not os.path.exists(FILE_RIWAYAT) or os.path.getsize(FILE_RIWAYAT) == 0
    with open(FILE_RIWAYAT, "a", encoding="utf-8") as f:
        if baru:
            f.write(GARIS_RIWAYAT + "\n")
            f.write(f"| {'Waktu':<19} | {'ID Transaksi':<18} | {'Nominal Transaksi':<17} |\n")
            f.write(GARIS_RIWAYAT + "\n")
        f.write(f"| {waktu.strftime('%Y-%m-%d %H:%M:%S'):<19} | {id_trx:<18} "f"| {rupiah(total):<17} |\n")
        f.write(GARIS_RIWAYAT + "\n")

def tampilkan_riwayat():
    if not os.path.exists(FILE_RIWAYAT):
        print("\nBelum ada transaksi yang tercatat.")
        return
    with open(FILE_RIWAYAT, "r", encoding="utf-8") as f:
        print("\n" + f.read())

#TRANSACTION FLOW
def transaksi_baru():
    print("\n=== TRANSAKSI BARU ===")
    kasir = input_teks("Nama kasir      : ")
    items = []
    while True:
        print(f"\nProduk ke-{len(items) + 1}")
        nama = input_teks("  Nama produk   : ")
        harga = input_angka("  Harga produk  : Rp. ")
        qty = input_angka("  Jumlah        : ")
        items.append((nama, harga, qty))
        lagi = input("Tambah produk lain? (y/n): ").strip().lower()
        if lagi != "y":
            break

    waktu = datetime.now()
    id_trx = buat_id_transaksi(kasir, waktu)
    total = sum(harga * qty for _, harga, qty in items)
    isi = susun_invoice(id_trx, waktu, kasir, items, total)
    path = simpan_invoice(id_trx, isi)
    catat_riwayat(waktu, id_trx, total)

    print("\nTransaksi berhasil!")
    print(f"ID Transaksi : {id_trx}")
    print(f"Invoice      : {path}\n")
    print(isi)

#SEARCHING INVOICE
def cari_invoice():
    print("\n=== CARI INVOICE ===")
    id_trx = input_teks("Masukkan ID transaksi: ")
    if id_trx.lower().endswith(".txt"):
        id_trx = id_trx[:-4] #jika kasir mengetik .txt maka akan terhapus
    path = os.path.join(FOLDER_INVOICE, id_trx + ".txt")
    if not os.path.isfile(path):
        print(f"\nInvoice dengan ID '{id_trx}' tidak ditemukan.")
        return
    with open(path, "r", encoding="utf-8") as f: #hanya untuk dibaca dan ditampilkan
        print("\n" + f.read())

#MENU UTAMA (INPUT AND OUTPUT)
def main():
    while True:
        print("=" * 40)
        print("          APLIKASI KASIR SEDERHANA")
        print("=" * 40)
        print("1. Transaksi baru")
        print("2. Cari invoice")
        print("3. Lihat riwayat transaksi")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            transaksi_baru()
        elif pilihan == "2":
            cari_invoice()
        elif pilihan == "3":
            tampilkan_riwayat()
        elif pilihan == "0":
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print("\nPilihan tidak valid.\n")

main()