def deteksi_anomali_email(email):
    masalah = []

    #Aturan 1: hanya satu '@'
    jumlah_at = email.count("@")
    if jumlah_at != 1:
        masalah.append("Harus memiliki tepat satu karakter @.")
    #Aturan 3: tidak boleh ada spasi
    if " " in email:
        masalah.append("Tidak boleh mengandung spasi.")

    if jumlah_at != 1:
        return masalah

    local, domain = email.split("@")
    #Aturan 2: local & domain tidak boleh kosong
    if local == "" or domain == "":
        masalah.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")
    #Aturan 4: aturan titik pada local
    if local.startswith(".") or local.endswith(".") or ".." in local:
        masalah.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")
    #Aturan 5: aturan titik pada domain
    if "." not in domain:
        masalah.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        masalah.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
    #Aturan 7: domain resmi (.ac.id sudah tercakup oleh .id, ditulis tetap eksplisit)
    if not (email.lower().endswith(".com")
            or email.lower().endswith(".id")
            or email.lower().endswith(".ac.id")):
        masalah.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return masalah

#Validasi email, cetak daftar email valid
def cetak_daftar(daftar_email_valid, karakter_border):
    """Bentuk string multi-baris berbingkai; lebar mengikuti email terpanjang."""
    if len(daftar_email_valid) == 0:
        return "(Belum ada email valid)"

    border = karakter_border[0] if karakter_border != "" else "="

    terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > terpanjang:
            terpanjang = len(email)

    garis = "+" + border * (terpanjang + 2) + "+"

    hasil = garis
    for email in daftar_email_valid:
        hasil += "\n| " + email.ljust(terpanjang) + " |"
    hasil += "\n" + garis
    return hasil

#Input dan Output
def main():
    print("--- Sistem Pencatatan email valid ---")
    karakter_border = input("Masukkan border dengan karakter bebas: ")
    print()
    print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

    daftar_valid = []
    daftar_valid_kecil = []  #untuk cek duplikat (tidak peka huruf besar/kecil)

    while True:
        email = input("Masukkan email: ")
        if email.strip().lower() == "tutup":
            break

        masalah = deteksi_anomali_email(email)

        #Aturan 6: tidak boleh duplikat (hanya relevan jika email lolos aturan lain)
        if len(masalah) == 0 and email.lower() in daftar_valid_kecil:
            masalah.append("Email sudah terdaftar (Duplikat).")
        #Jika lolos semua aturan, simpan email valid
        if len(masalah) == 0:
            daftar_valid.append(email)
            daftar_valid_kecil.append(email.lower())
            print(">> Email VALID!")
        else:
            print(">> Email DITOLAK karena:")
            for pesan in masalah:
                print("   - " + pesan)

    print()
    print("--- HASIL EMAIL VALID ---")
    print(cetak_daftar(daftar_valid, karakter_border))

main()