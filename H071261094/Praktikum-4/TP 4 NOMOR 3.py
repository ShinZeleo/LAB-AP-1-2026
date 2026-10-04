def hitung_mundur(angka):
    """Mencetak angka dari 'angka' sampai 0 secara rekursif."""
    print(angka)
    if angka == 0:                 
        print("Luncurkan!")
        return
    hitung_mundur(angka - 1)       

def main():
    while True:
        try:
            angka_awal = int(input("Masukkan angka awal hitung mundur: "))
            if angka_awal < 0:
                print("Input tidak valid, angka tidak boleh negatif.")
            else:
                break
        except ValueError:
            print("Input tidak valid, masukkan angka yang benar.")

    hitung_mundur(angka_awal)

main()