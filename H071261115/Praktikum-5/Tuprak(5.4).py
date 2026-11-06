DOMAIN_RESMI = (".com", ".id", ".ac.id")


def deteksi_anomali_email(email):
    error = []

    # Aturan 1: tepat satu '@'
    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error

    local, domain = email.split("@")

    # Aturan 2: local & domain tidak kosong
    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    # Aturan 3: tidak boleh ada spasi
    if " " in email:
        error.append("Email tidak boleh mengandung spasi.")

    # Aturan 4: titik pada local
    if local.startswith(".") or local.endswith(".") or ".." in local:
        error.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    # Aturan 5: titik pada domain
    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    # Aturan 7: domain resmi
    if not email.endswith(DOMAIN_RESMI):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    terpanjang = 0
    for e in daftar_email_valid:
        if len(e) > terpanjang:
            terpanjang = len(e)
    lebar = terpanjang + 2
    garis = "+" + karakter_border * lebar + "+"

    hasil = garis + "\n"
    for e in daftar_email_valid:
        hasil += "| " + e + " " * (terpanjang - len(e)) + " |\n"
    hasil += garis
    return hasil


def main():
    print("--- Sistem Pencatatan email valid ---")
    border = input("Masukkan border dengan karakter bebas: ")
    print()
    print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

    valid = []
    while True:
        email = input("Masukkan email: ")
        if email.strip().lower() == "tutup":
            break

        error = deteksi_anomali_email(email)
        # Aturan 6: duplikat
        if not error and email in valid:
            error.append("Email sudah terdaftar (Duplikat).")

        if error:
            print(">> Email DITOLAK karena:")
            for e in error:
                print("   -", e)
        else:
            print(">> Email VALID!")
            valid.append(email)

    print()
    print("--- HASIL EMAIL VALID ---")
    if valid:
        print(cetak_daftar(valid, border))
    else:
        print("(belum ada email valid)")


if __name__ == "__main__":
    main()