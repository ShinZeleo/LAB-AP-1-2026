import time 

def hitung_mundur (n: int):
    if n == 0:
        print (0)
        print ("Luncurkan!")
    else:
        print (n)
        time.sleep (1)
        hitung_mundur(n-1)

while True:
    try:
        angka_awal = int(input("Masukkan angka awal hitung mundur: "))

        if angka_awal < 0:
            print ("Input tidak valid, angka tidak boleh negatif.")
        hitung_mundur(angka_awal)
        break 

    except ValueError:
        print("Input tidak valid, masukkan angka bulat.")