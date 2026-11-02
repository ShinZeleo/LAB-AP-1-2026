import re

def bersihkan_nomor(nomor):
    return re.sub(r'[\s\-]', '', nomor)

def validasi_nomor(nomor):
    pattern = r'^\d{10,13}$'
    if re.match(pattern, nomor):
        return True
    return False


print("=== Pembersihan Data Nomor Telepon ===\n")
jumlah = int(input("Masukkan jumlah data: "))

data_awal = []
data_bersih = []
nomor_valid = []

for i in range(1, jumlah + 1):
    nomor = input(f"Nomor ke-{i}: ")

    hasil = bersihkan_nomor(nomor)
    data_awal.append(nomor)
    data_bersih.append(hasil)

    if validasi_nomor(hasil):
        nomor_valid.append(hasil)

print("=== Hasil Pembersihan ===\n")
for i in range(jumlah):
    print(f"Data {i + 1}:")
    print("Sebelum :", data_awal[i])
    print("Sesudah :", data_bersih[i])
    if validasi_nomor(data_bersih[i]):
        print("Status  : Valid")
    else:
        print("Status  : Tidak valid")

print("Jumlah nomor valid:", len(nomor_valid))