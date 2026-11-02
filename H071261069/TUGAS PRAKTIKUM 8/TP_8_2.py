import re

def validasi_username(username):
    pattern = r'^\w{5,12}$'
    return (re.match(pattern, username))

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.\n")

username_valid_list = []

while True:
    username = input("Masukkan username: ")
    if username == "SELESAI":
        break
    
    if validasi_username(username):
        print("Username tersedia.\n")
        username_valid_list.append(username)
    else:
        print("Username tidak valid!\n")

print("\n=== Rekapitulasi ===")
print("Username valid:")
for i, name in enumerate(username_valid_list, 1):
    print(f"{i}. {name}")
print(f"\nJumlah username valid: {len(username_valid_list)}")
