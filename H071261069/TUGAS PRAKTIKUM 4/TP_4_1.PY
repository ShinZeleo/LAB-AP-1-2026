def kasir():
    print('Selamat datang di Kasir Minimarket!')
    status_member = input('Apakah Anda member? (y/n): ').lower()
    total = 0
    while True:
        nama_barang = input('Masukkan nama barang (kosongkan untuk selesai): ')
        if nama_barang:
            harga = int(input('Harga barang: '))
            jumlah = int(input('Jumlah barang: '))
            subtotal = harga * jumlah
            if status_member == 'y':
                subtotal = subtotal - (harga * jumlah * 10//100)  
            else:
                subtotal
        else:
            nama_barang = ''
            print(f'Total belanja: Rp{total}')
            break
            
        total += subtotal
        print(f'Subtotal {nama_barang}: Rp{subtotal}')
    return 
   
kasir() 


    

