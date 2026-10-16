def hitung_rincian_kembalian(jumlah_kembalian):
    """Menghitung rincian lembaran uang untuk sejumlah kembalian tertentu."""
    daftar_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    
    rincian = {} 
    sisa_kembalian = jumlah_kembalian
    
    for pecahan in daftar_pecahan:
        if sisa_kembalian >= pecahan:
            jumlah_lembar = sisa_kembalian // pecahan  
            rincian[pecahan] = jumlah_lembar
            sisa_kembalian = sisa_kembalian % pecahan   
    
    return rincian

total_harga = int(input("Masukkan total harga: "))
uang_diberikann = int(input("Masukkan uang yang diberikan: "))

if uang_diberikann < total_harga:
    print("Uang yang diberikan tidak cukup!")
else:
    kembalian = uang_diberikann - total_harga
    print(f"\nKembalian: Rp {kembalian:,}")
    
    if kembalian == 0:
        print("Tidak ada kembalian (uang pas).")
    else:
        rincian_lembaran = hitung_rincian_kembalian(kembalian)
        print("\nRincian kembalian:")
        for pecahan, lembar in rincian_lembaran.items():
            print(f"{lembar} lembar Rp {pecahan:,}")