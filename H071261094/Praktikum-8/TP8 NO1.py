import re


def validasi_nim(nim):
    pola = r"^H071\d{6}$"
    hasil = re.match(pola, nim)
    if hasil:
        return True
    else:
        return False


def validasi_email(email):
    pola = r"^[A-Za-z0-9_.]+@[A-Za-z0-9\.]+\.[A-Za-z]+$"
    hasil = re.match(pola, email)
    if hasil:
        return True
    else:
        return False


def validasi_telepon(telp):
    pola = r"^\d{10,13}$"
    hasil = re.match(pola, telp)
    if hasil:
        return True
    else:
        return False


print("=== Validasi Data Mahasiswa ===")
print()

nim = input("Masukkan NIM       : ").strip()
email = input("Masukkan Email     : ").strip()
telp = input("Masukkan No. Telp  : ").strip()

nim_valid = validasi_nim(nim)
email_valid = validasi_email(email)
telp_valid = validasi_telepon(telp)

print()
print("--- Hasil Validasi ---")

if nim_valid:
    print("NIM         : Valid")
else:
    print("NIM         : Tidak valid")
    print("Format NIM tidak valid!")

if email_valid:
    print("Email       : Valid")
else:
    print("Email       : Tidak valid")
    print("Format email tidak valid!")

if telp_valid:
    print("No. Telepon : Valid")
else:
    print("No. Telepon : Tidak valid")
    print("Nomor telepon tidak valid!")

print()
if nim_valid and email_valid and telp_valid:
    print("Data mahasiswa berhasil diverifikasi!")