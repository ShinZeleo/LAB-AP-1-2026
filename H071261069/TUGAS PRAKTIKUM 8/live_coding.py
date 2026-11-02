import re

def cari_angka(pesan):
    pattern = r'\d+'
    hasil = re.findall(pattern,pesan)
    return hasil
 
def cari_email(pesan):
    pattern = r'\w+@\w+.\w+'
    hasil = re.findall(pattern, pesan)
    return hasil

def cari_nomor(pesan):
    pattern = r'\d{10,13}'    
    hasil = re.findall(pattern, pesan)
    return hasil

pesan = input("Masukkan pesan: \n")

angka = cari_angka(pesan)
email = cari_email(pesan)
nomor = cari_nomor(pesan)

if angka and email and nomor:
    print()
    print("=== HASIL PENCARIAN ===")
    print(f"Angka ditemukan: {angka}")
    print(f"Email ditemukan: {email}")
    print(f"Nomor telepon ditemukan: {nomor}")
else:
    print("Tidak ada data yang ditemukan.")

if angka and email and nomor:
    print()
    print(f"Jumlah angka: {len(angka)}")
    print(f"Jumlah email: {len(email)}")
    print(f"Jumlah nomor telepon: {len(nomor)}")
else:
    print("")