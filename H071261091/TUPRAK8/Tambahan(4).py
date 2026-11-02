import re

def cari_alamat_email(pesan):
    pattern = r'\w+@[\w\.]+\.\w+'
    hasil = re.findall(pattern, pesan)
    return hasil

def cari_nomor_telepon(pesan):
    pattern = r'\d{10,13}'
    hasil = re.findall(pattern, pesan)
    return hasil

print ("=== Pencarian Informasi Pesan ===")
pesan = input("Masukkan pesan: \n")

print ("Angka ditemukan: ", re.findall(r'\d+', pesan))
print ("Email ditemukan: ", cari_alamat_email(pesan))
print ("Nomor telepon ditemukan: ", cari_nomor_telepon(pesan))

print ("Jumlah angka: ", len(re.findall(r'\d+', pesan)))
print ("Jumlah email: ", len(cari_alamat_email(pesan)))
print ("Jumlah nomor telepon: ", len(cari_nomor_telepon(pesan)))