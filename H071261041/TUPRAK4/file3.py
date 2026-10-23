def hitung_mundur(n):
    print(n)
    if n == 0:
        print("luncurkan!")
    else:
        hitung_mundur(n - 1)

while True:
    angka = int(input("masukkan angka awal hitung mundur: "))
    if angka < 0:
        print("input tidak valid,angka tidak boleh negatif")
    else:
        break

hitung_mundur(angka)

       
         