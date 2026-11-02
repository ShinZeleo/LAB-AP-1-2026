import re

def validasi_username(username):
    pattern = r'^[a-zA-Z][\w]{4,12}$'
    if re.match(pattern, username):
        daftar_username.append(username)
        return "Username Tersedia."
    return "Username Tidak Valid!"

daftar_username = []

print ("=== Registrasi Username ===")
while True:
    username = input("Masukkan username (SELESAI untuk berhenti): ")
    if username.upper() == "SELESAI":
        print("=== Rekapitulasi ===")
        for i in range(len(daftar_username)):
            print(f"{i+1}. {daftar_username[i]}")
        print("Jumlah username valid:", len(daftar_username))
        break
    print(validasi_username(username))