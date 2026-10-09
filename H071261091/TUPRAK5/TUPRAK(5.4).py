alfabet = "abcdefghijklmnopqrstuvwxyz"
def deteksi_anomali_email(email):
    daftar_error = []

    # Aturan 1: tepat satu @
    if email.count("@") != 1:
        daftar_error.append("Harus memiliki tepat satu karakter @.")
        return daftar_error

    posisi_at = email.find("@")
    bagian_local = email[:posisi_at]
    bagian_domain = email[posisi_at + 1:]

    # Aturan 2: local dan domain tidak kosong
    if bagian_local == "" or bagian_domain == "":
        daftar_error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    # Aturan 3: tidak ada spasi
    if " " in email:
        daftar_error.append("Email tidak boleh mengandung spasi.")

    # Aturan 4: aturan titik pada local
    if bagian_local.startswith(".") or bagian_local.endswith(".") or ".." in bagian_local:
        daftar_error.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    # Aturan 5: aturan titik pada domain
    if "." not in bagian_domain:
        daftar_error.append("Bagian domain wajib memiliki minimal satu titik.")
    elif ".." in bagian_domain or bagian_domain.endswith("."):
        daftar_error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    # Aturan 7: domain resmi
    berakhir_resmi = email.endswith(".com") or email.endswith(".id") or email.endswith(".ac.id")
    if not berakhir_resmi:
        daftar_error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return daftar_error


def cetak_daftar(daftar_email_valid, karakter_border):
    lebar_terpanjang = 0
    for email in daftar_email_valid:
        if len(email) > lebar_terpanjang:
            lebar_terpanjang = len(email)

    garis_bingkai = "+" + karakter_border * (lebar_terpanjang + 2) + "+"

    hasil = garis_bingkai
    for email in daftar_email_valid:
        spasi_pengisi = " " * (lebar_terpanjang - len(email))
        hasil = hasil + "\n| " + email + spasi_pengisi + " |"
    hasil = hasil + "\n" + garis_bingkai
    return hasil


print("--- Sistem Pencatatan email valid ---")
karakter_border = input("Masukkan border dengan karakter bebas: ")
print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_email_valid = []
while True:
    email = input("Masukkan email: ")
    if email == "tutup":
        break

    daftar_error = deteksi_anomali_email(email)
    if email in daftar_email_valid: # Aturan 6: duplikat
        daftar_error.append("Email sudah terdaftar (Duplikat).")

    if len(daftar_error) == 0:
        print(">> Email VALID!")
        daftar_email_valid.append(email)
    else:
        print(">> Email DITOLAK karena:")
        for pesan_error in daftar_error:
            print(f"- {pesan_error}")

print("\n--- HASIL EMAIL VALID ---")
print(cetak_daftar(daftar_email_valid, karakter_border))