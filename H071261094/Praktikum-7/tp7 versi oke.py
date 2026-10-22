import datetime
import random
import os

FOLDER_INVOICE = "invoices"
FILE_HISTORY = "trx_history.txt"
LEBAR_FILE = 76  
LEBAR_TERM = 65  

def siapkan_folder():
    os.makedirs(FOLDER_INVOICE, exist_ok=True)

def format_rupiah(nominal):
    return f"Rp{nominal:,}".replace(",", ".")

def input_positif(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            if nilai <= 0:
                print("Input harus lebih dari 0.")
                continue
            return nilai
        except ValueError:
            print("Input harus berupa bilangan bulat.")

def buat_id_transaksi(nama_kasir, waktu):
    inisial = "".join(kata[0] for kata in nama_kasir.split()).upper()
    bagian_waktu = waktu.strftime("%y%m%d%H%M")
    
    while True:
        angka_acak = random.randint(100, 999)
        id_transaksi = inisial + bagian_waktu + str(angka_acak)
        nama_file = id_transaksi + ".txt"
        path_file = os.path.join(FOLDER_INVOICE, nama_file)
        
        if not os.path.exists(path_file):
            return id_transaksi, path_file

def buat_invoice(nama_kasir, waktu, id_transaksi, produk, total_nominal_transaksi):
    nama_file = id_transaksi + ".txt"
    path_file = os.path.join(FOLDER_INVOICE, nama_file)
    
    try:
        with open(path_file, "x") as file:
            file.write("TOKO FATHUR".center(LEBAR_FILE) + "\n")
            file.write("=" * LEBAR_FILE + "\n")
            file.write(f"Nama Kasir      : {nama_kasir}\n")
            file.write(f"Waktu Transaksi : {waktu.strftime('%d/%m/%y %H:%M:%S')}\n")
            file.write(f"ID Transaksi    : {id_transaksi}\n")
            file.write("=" * LEBAR_FILE + "\n\n")
            file.write("DAFTAR PRODUK".center(LEBAR_FILE) + "\n\n")
            
            file.write("-" * LEBAR_FILE + "\n")
            file.write(
                f"| {'Nama Produk':<28} | {'Harga':>12} | "
                f"{'Jumlah':>6} | {'Subtotal':>14} |\n"
            )
            file.write("-" * LEBAR_FILE + "\n")
            
            for item in produk:
                nama = item["nama"][:28]
                file.write(
                    f"| {nama:<28} | "
                    f"{format_rupiah(item['harga']):>12} | "
                    f"{item['jumlah']:>6} | "
                    f"{format_rupiah(item['subtotal']):>14} |\n"
                )
                
            file.write("-" * LEBAR_FILE + "\n")
            file.write(
                f"| {'TOTAL TRANSAKSI':<50} | "
                f"{format_rupiah(total_nominal_transaksi):>18} |\n"
            )
            file.write("=" * LEBAR_FILE + "\n\n")
            file.write("TERIMA KASIH TELAH BERBELANJA".center(LEBAR_FILE) + "\n")
            
        return path_file
    except OSError as error:
        print(f"Gagal menyimpan invoice: {error}")
        return None

def siapkan_riwayat():
    if not os.path.exists(FILE_HISTORY):
        try:
            with open(FILE_HISTORY, "w") as file:
                file.write("RIWAYAT TRANSAKSI".center(LEBAR_FILE) + "\n")
                file.write("=" * LEBAR_FILE + "\n")
                file.write(
                    f"| {'Waktu':<19} | "
                    f"{'ID Transaksi':<25} | "
                    f"{'Nominal Transaksi':>23} |\n"
                )
                file.write("=" * LEBAR_FILE + "\n")
        except OSError as error:
            print(f"Gagal membuat file riwayat: {error}")

def catat_riwayat(waktu, id_transaksi, nominal):
    try:
        with open(FILE_HISTORY, "a") as file:
            file.write(
                f"| {waktu.strftime('%Y-%m-%d %H:%M:%S'):<19} | "
                f"{id_transaksi:<25} | "
                f"{format_rupiah(nominal):>23} |\n"
            )
            file.write("=" * LEBAR_FILE + "\n")
        return True
    except OSError as error:
        print(f"Gagal mencatat riwayat transaksi: {error}")
        return False

def transaksi_baru(nama_kasir):
    produk = []
    total_nominal_transaksi = 0
    
    while True:
        nama_produk = input(f"{'Masukkan nama produk':<25} : ").strip()
        if not nama_produk:
            print("Nama produk tidak boleh kosong.")
            continue
            
        harga_produk = input_positif(f"{'Masukkan harga produk':<25} : ")
        jumlah_produk = input_positif(f"{'Masukkan jumlah produk':<25} : ")
        
        subtotal = harga_produk * jumlah_produk
        total_nominal_transaksi += subtotal
        
        produk.append({
            "nama": nama_produk,
            "harga": harga_produk,
            "jumlah": jumlah_produk,
            "subtotal": subtotal
        })
        
        print("=" * LEBAR_TERM)
        tambah = input(f"{'Tambah produk? (y/t)':<25} : ").strip().lower()
        while tambah not in ("y", "t"):
            tambah = input(f"{'Masukkan y atau t':<25} : ").strip().lower()
            
        print("=" * LEBAR_TERM)
        if tambah == "t":
            break
            
    waktu = datetime.datetime.now()
    id_transaksi, _ = buat_id_transaksi(nama_kasir, waktu)
    
    hasil_invoice = buat_invoice(
        nama_kasir, waktu, id_transaksi, produk, total_nominal_transaksi
    )
    
    if hasil_invoice is None:
        print("Transaksi belum berhasil disimpan.")
        return
        
    catat_riwayat(waktu, id_transaksi, total_nominal_transaksi)
    
    print("TRANSAKSI BERHASIL".center(LEBAR_TERM))
    print("=" * LEBAR_TERM)

def cari_invoice():
    id_dicari = input(f"{'Masukkan ID transaksi':<25} : ").strip()
    print("=" * LEBAR_TERM)
    
    if not id_dicari:
        print("ID transaksi tidak boleh kosong.")
        return
        
    if (
        os.path.basename(id_dicari) != id_dicari
        or "/" in id_dicari
        or "\\" in id_dicari
        or id_dicari.lower().endswith(".txt")
    ):
        print("Masukkan ID transaksi saja, tanpa path atau .txt.")
        return
        
    nama_file = id_dicari + ".txt"
    path_file = os.path.join(FOLDER_INVOICE, nama_file)
    
    if not os.path.isfile(path_file):
        print("Transaksi tidak ditemukan.")
        return
        
    try:
        with open(path_file, "r") as file:
            isi_invoice = file.read()
        print(isi_invoice)
    except OSError as error:
        print(f"Gagal membaca invoice: {error}")

def main():
    siapkan_folder()
    siapkan_riwayat()
    
    print("=" * LEBAR_TERM)
    print("SELAMAT DATANG".center(LEBAR_TERM))
    print("=" * LEBAR_TERM)
    
    nama_kasir = input(f"{'Masukkan nama kasir':<25} : ").strip()
    while not nama_kasir:
        print("Nama kasir tidak boleh kosong.")
        nama_kasir = input(f"{'Masukkan nama kasir':<25} : ").strip()
        
    print("=" * LEBAR_TERM)
    
    while True:
        print("Pilih opsi:")
        print("1. Transaksi baru")
        print("2. Cari transaksi")
        print("3. Keluar")
        print("=" * LEBAR_TERM)
        
        pilihan = input(f"{'Masukkan opsi pilihan':<25} : ").strip()
        print("=" * LEBAR_TERM)
        
        if pilihan == "1":
            transaksi_baru(nama_kasir)
        elif pilihan == "2":
            cari_invoice()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
            print("=" * LEBAR_TERM)

main()