import re


def validasi_username(username):
    pola = r"^[A-Za-z][A-Za-z0-9_]{4,11}$"
    hasil = re.match(pola, username)
    if hasil:
        return True
    else:
        return False


print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")
print()

daftar_valid = []

while True:
    username = input("Masukkan username: ").strip()

    if username == "SELESAI":
        break

    if validasi_username(username):
        print("Username tersedia.")
        daftar_valid.append(username)
    else:
        print("Username tidak valid!")
    print()

print("=== Rekapitulasi ===")
if len(daftar_valid) == 0:
    print("Belum ada username yang valid.")
else:
    print("Username valid:")
    nomor = 1
    for nama in daftar_valid:
        print(f"{nomor}. {nama}")
        nomor += 1

print()
print("Jumlah username valid:", len(daftar_valid))