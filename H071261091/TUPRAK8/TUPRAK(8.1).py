import re
def validasi_nim(nim):
    pattern = r'^H071\d{6}$'
    if re.match(pattern, nim):
        return "Valid"
    return "Tidak Valid"

def validasi_email(email):
    pattern = r'^\w+@[\w\.]+\.\w+$'
    if re.match(pattern, email):
        return "Valid"
    return "Tidak Valid"

def validasi_no_telp(no_telp):
    pattern = r'^\d{10,13}$'
    if re.match(pattern, no_telp):
        return "Valid"
    return "Tidak Valid"


print ("=== Validasi Data Mahasiswa ===")

nim = input("Masukkan NIM       : ")
email = input("Masukkan Email     : ")
no_telp = input("Masukkan No. Telp  : ")

print ("=== Hasil Validasi ===")

print(f"NIM             : {validasi_nim(nim)}")
print(f"Email           : {validasi_email(email)}")
print(f"No. Telp        : {validasi_no_telp(no_telp)}")

if validasi_nim(nim) == "Valid" and validasi_email(email) == "Valid" and validasi_no_telp(no_telp) == "Valid":
    print ("Data mahasiswa berhasil diverifikasi!")