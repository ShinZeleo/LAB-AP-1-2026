import re

print("=== Pencarian Informasi Pesan")
print()
teks = input("masukkan pesan: \n")

angka = re.findall(r'\d+', teks)
email = re.findall(r'\w+@[\w\.]+\.\w+', teks)
telepon = re.findall(r'\d{10,13}', teks)

print("--- Hasil Pencarian---")
print("Angka ditemukan:", angka )
print("Email ditemukan:", email)
print("Nomor telepon ditemukan:", telepon)

print()
print("Jumlah angka                 :", len(angka))
print("Jumlah email                 :", len(email))
print("Jumlah nomor telepon         :", len(telepon))
