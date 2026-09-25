saldo_awal =  500000

while True:
    print ("Menu")
    print ("1. Cek Saldo")
    print ("2. Tarik Tunai")
    print ("3. Setor Tunai")
    print ("4. Keluar")

    pilihan = input("Pilih Menu (1-4): ")

    if pilihan == "1":
        print(f"Saldo saat ini: {saldo_awal} ")
    
    elif pilihan == "2":
        try:
            tarik = int(input("Masukkan nominal penarikan: Rp"))
            if tarik > saldo_awal :
                print("Saldo tidak cukup !")
                continue
        
            elif tarik <= 0 :
                print("Nominal harus lebih besar")

            else:
                saldo_awal -= tarik
                print (f"Penarikan berhasil. Saldo saat ini: {saldo_awal} ")

        except ValueError:
            print ("ok")

    elif pilihan == "3":
        setor = int(input("Masukkan nilai setoran: "))
        saldo_awal += setor
        print(f"Setoran berhasil. Saldo saat ini: {saldo_awal}")

    elif pilihan == "4":
        print ("Terima kasih telah menggunakan ATM. ")
        break

    else:
        print ("Pilihan tidak valid")
