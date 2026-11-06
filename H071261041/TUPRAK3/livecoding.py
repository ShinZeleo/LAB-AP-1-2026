jumlah_angka =int(input("masukkan jumlah baris: "))

for baris in range(1, jumlah_angka + 1):
    for angka in range(1, baris + 1):
     print(angka, end=" ")
    print()