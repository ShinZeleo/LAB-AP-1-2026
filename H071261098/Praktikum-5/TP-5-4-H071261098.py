daftar_email_valid = []

def deteksi_anomali_email(email):
    char = ["@", ".", " ", ['.com', '.ac', '.ac.id']]
    simbol_wajib = char[0]
    titik = char[1]
    spasi = char[2]
    list_domain = char[3]
    list_pesan = []
    
    if spasi in email:
        pesan = "email tidak boleh mengandung spasi"
        list_pesan.append(pesan)
        
    if email.count(simbol_wajib) != 1:
        pesan = "Harus memiliki tepat satu karakter @"
        list_pesan.append(pesan)
    
    if email.count(simbol_wajib) == 1:
        bagian_local, bagian_domain = email.split(simbol_wajib)
        
        if bagian_local == "" or bagian_domain == "":
            pesan = "Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong."
            list_pesan.append(pesan)
            
        if titik not in bagian_domain:
            pesan = "Bagian domain wajib memiliki minimal 1 titik."
            list_pesan.append(pesan)
    else:
        if titik not in email:
            pesan = "Bagian domain wajib memiliki 1 titik."
            list_pesan.append(pesan)
        
    domain_valid = False
    for domain in list_domain:
        if email.endswith(domain):
            domain_valid = True
            break
        
    if not domain_valid:
        pesan = "wajib berakhiran .com, .ac, .ac.id"
        list_pesan.append(pesan)
        
    if email in daftar_email_valid:
        pesan = "Email sudah terdaftar"
        list_pesan.append(pesan)
                
    return list_pesan

def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        print("\nTidak ada email valid yang tercatat.")
        return

    total_index_email = [] 
    for i in daftar_email_valid:
        panjang_email = len(i)
        total_index_email.append(panjang_email)
        
    index_terpanjang = max(total_index_email)
    
    padding = 2
    lebar_kotak_dalam = index_terpanjang + (padding * 2)
    
    print("\n--- HASIL EMAIL VALID ---")
    
    print("+" + karakter_border * lebar_kotak_dalam + "+")
    
    for email in daftar_email_valid:
        isi_baris = email.center(lebar_kotak_dalam)
        print(f"| {isi_baris}|")
        
    print("+" + karakter_border * lebar_kotak_dalam + "+")

print("--- Sistem Pencatatan Email Valid")
tipe_border = input("Masukkan tipe border: ")

print("ketik 'tutup' untuk mengakhiri dan mencetak email")

while True:
    email = input("Masukkan email: ").lower()
    
    if email == 'tutup':
        break
    
    errors = deteksi_anomali_email(email)
    
    
    if len(errors) > 0:
        print(">> Email Ditolak Karena")
        for error in errors:
            print("- ",error)
    else:
        print(">> Email Valid")
        daftar_email_valid.append(email)
        
cetak_daftar(daftar_email_valid,tipe_border)
