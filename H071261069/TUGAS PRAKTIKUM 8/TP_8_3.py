import re

print("=== Pembersihan Data Nomor Telepon ===\n")

jumlah = int(input("Masukkan jumlah data: "))

data_nomor = []
for i in range(1, jumlah + 1):
    nomor = input(f"\nNomor ke-{i}: ")
    data_nomor.append(nomor)

nomor_valid_list = []

print("\n--- Hasil Pembersihan ---")

for i, nomor in enumerate(data_nomor, 1):
    nomor_bersih = re.sub(r'[\s-]', '', nomor)
    is_valid = (re.match(r'^\d{10,13}$', nomor_bersih))
    
    print(f"\nData {i}:")
    print(f"Sebelum : {nomor}")
    print(f"Sesudah : {nomor_bersih}")
    print(f"Status  : {'Valid' if is_valid else 'Tidak Valid'}")
    
    if is_valid:
        nomor_valid_list.append(nomor_bersih)

print(f"\nJumlah nomor valid: {len(nomor_valid_list)}")
