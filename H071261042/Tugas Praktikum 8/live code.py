import re
print("===Pencarian Informasi Pesan===")
print()
pesan = input ("Masukkan pesan: ")

angka = re.findall(r'\d+', pesan)
email = re.findall(r'[A-Za-z0-9.]+@[A-Za-z0-9-]+\.[A-Za-z0-9.]+', pesan)
telepon = re.findall(r'\b08\d{8,11}\b', pesan)
 
print("---Hasil Pencarian---")
if angka:
    print("angka ditemukan: ", angka)
else:
    print("tidak ada data yang ditemukan.")

if email:
    print("email ditemukan: ", email)
else:
    print("tidak ada data yang ditemukan.")

if telepon:
    print("nomor telepon ditemukan: ", telepon)
else:
    print("tidak ada data yang ditemukan.")
print()

print("jumlah angka: ", len(angka))
print("jumlah email: ", len(email))
print("jumlah nomor telepon: ", len(telepon))
