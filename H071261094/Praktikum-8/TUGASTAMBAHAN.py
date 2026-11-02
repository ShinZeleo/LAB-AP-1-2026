import re

def cari_email(pesan):
    pola = r'[\w.]+@[\w.]+\.\w+'
    hasil = re.findall(pola, pesan)
    return hasil

def cari_angka(pesan):
    pola = r'\d+'
    hasil = re.findall(pola, pesan)
    return hasil

def cari_nomor(pesan):
    pola = r'\b\d{10,13}\b'
    hasil = re.findall(pola, pesan)
    return hasil

print("Masukkan pesan:")
pesan = input()

angka = cari_angka(pesan)
email = cari_email(pesan)
telepon = cari_nomor(pesan)

print("\n--- Hasil Pencarian ---")
print(f"Angka ditemukan         : {angka}")
print(f"Email ditemukan         : {email}")
print(f"Nomor telepon ditemukan : {telepon}")

print()
print(f"Jumlah angka         : {len(angka)}")
print(f"Jumlah email         : {len(email)}")
print(f"Jumlah nomor telepon : {len(telepon)}")