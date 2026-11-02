import re

def validasi_nim(nim):
    pattern = r'^H071\d{6}$'
    return (re.match(pattern, nim))

def validasi_email(email):
    pattern = r'^\w+@\w+.\w+$'
    return (re.match(pattern, email))

def validasi_telepon(telepon):
    pattern = r'^\d{10,13}$'
    return (re.match(pattern, telepon))

print("=== Validasi Data Mahasiswa ===\n")

nim = input("Masukkan NIM: ")
email = input("Masukkan Email: ")
telepon = input("Masukkan No. Telp: ")

print("\n--- Hasil Validasi ---")

nim_valid = validasi_nim(nim)
email_valid = validasi_email(email)
telepon_valid = validasi_telepon(telepon)

print(f"NIM : {'Valid' if nim_valid else 'Format NIM tidak valid!'}")
print(f"Email : {'Valid' if email_valid else 'Format email tidak valid!'}")
print(f"No. Telepon : {'Valid' if telepon_valid else 'Nomor telepon tidak valid!'}")

if nim_valid and email_valid and telepon_valid:
    print("\nData mahasiswa berhasil diverifikasi!")

