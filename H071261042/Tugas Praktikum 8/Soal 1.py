import re

#BASE
def validasi_nim(nim):
    return re.fullmatch(r"H071\d{6}", nim) is not None

def validasi_email(email):
    pola = r"[A-Za-z0-9._]+@([A-Za-z0-9-]+\.)+[A-Za-z]{2,}"
    return re.fullmatch(pola, email) is not None  # username, @, nama domain, \.(titik asli), ekstensi domain

def validasi_telepon(telp):
    return re.fullmatch(r"\d{10,13}", telp) is not None

def status(valid):
    return "Valid" if valid else "Tidak valid"

#INPUT OUTPUT
print("=== Validasi Data Mahasiswa ===\n")
nim = input("Masukkan NIM       : ").strip()
email = input("Masukkan Email     : ").strip()
telp = input("Masukkan No. Telp   : ").strip()

nim_ok = validasi_nim(nim)
email_ok = validasi_email(email)
telp_ok = validasi_telepon(telp)

print("\n--- Hasil Validasi ---")
print(f"NIM         : {status(nim_ok)}")
print(f"Email       : {status(email_ok)}")
print(f"No. Telepon : {status(telp_ok)}\n")

#PROCESSING BASE AND INPUT
if not nim_ok:
    print("Format NIM tidak valid!")
if not email_ok:
    print("Format email tidak valid!")
if not telp_ok:
    print("Nomor telepon tidak valid!")
if nim_ok and email_ok and telp_ok:
    print("Data mahasiswa berhasil diverifikasi!")