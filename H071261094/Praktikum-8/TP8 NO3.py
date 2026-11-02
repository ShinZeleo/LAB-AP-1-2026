import re


def bersihkan_nomor(nomor):
    pola = r"\s|-"
    hasil = re.sub(pola, "", nomor)
    return hasil


def validasi_nomor(nomor):
    pola = r"^\d{10,13}$"
    hasil = re.match(pola, nomor)
    if hasil:
        return True
    else:
        return False


print("=== Pembersihan Data Nomor Telepon ===")
print()

while True:
    try:
        jumlah = int(input("Masukkan jumlah data: "))
        if jumlah > 0:
            break
        print("Jumlah harus lebih dari 0!")
    except ValueError:
        print("Masukkan angka yang benar!")

data_sebelum = []
data_sesudah = []
nomor_valid = []

print()
for i in range(1, jumlah + 1):
    nomor = input(f"Nomor ke-{i}: ").strip()
    bersih = bersihkan_nomor(nomor)

    data_sebelum.append(nomor)
    data_sesudah.append(bersih)

    if validasi_nomor(bersih):
        nomor_valid.append(bersih)
    print()

print("--- Hasil Pembersihan ---")
print()
for i in range(jumlah):
    print(f"Data {i + 1}:")
    print("Sebelum :", data_sebelum[i])
    print("Sesudah :", data_sesudah[i])
    if validasi_nomor(data_sesudah[i]):
        print("Status  : Valid")
    else:
        print("Status  : Tidak valid")
    print()

print("Jumlah nomor valid:", len(nomor_valid))