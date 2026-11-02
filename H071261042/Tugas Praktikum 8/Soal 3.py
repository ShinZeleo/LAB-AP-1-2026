import re

#BASE
def bersihkan(nomor):
    return re.sub(r"[\s-]", "", nomor)

def validasi_telepon(nomor):
    return re.fullmatch(r"\d{10,13}", nomor) is not None

#INPUT AND OUTPUT
print("=== Pembersihan Data Nomor Telepon ===\n")
jumlah = int(input("Masukkan jumlah data: "))

sebelum = []
sesudah = []
nomor_valid = []

for i in range(1, jumlah + 1):
    nomor = input(f"\nNomor ke-{i}: ")
    bersih = bersihkan(nomor)
    sebelum.append(nomor)
    sesudah.append(bersih)
    if validasi_telepon(bersih):
        nomor_valid.append(bersih)

print("\n--- Hasil Pembersihan ---")
for i in range(jumlah):
    status = "Valid" if validasi_telepon(sesudah[i]) else "Tidak valid"
    print(f"\nData {i + 1}:")
    print(f"Sebelum : {sebelum[i]}")
    print(f"Sesudah : {sesudah[i]}")
    print(f"Status  : {status}")

print(f"\nJumlah nomor valid: {len(nomor_valid)}")