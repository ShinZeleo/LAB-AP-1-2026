def konversi_suhu(suhu, skala_asal, skala_tujuan):
    skala_asal = skala_asal.upper()
    skala_tujuan = skala_tujuan.upper()
    valid_skala = ["C", "F", "K"]
 
    if skala_asal not in valid_skala or skala_tujuan not in valid_skala:
        raise ValueError("Skala suhu tidak dikenali.")
 
    # Konversi skala asal ke Celsius terlebih dahulu
    if skala_asal == "C":
        celsius = suhu
    elif skala_asal == "F":
        celsius = (suhu - 32) * 5 / 9
    else:  # K
        celsius = suhu - 273.15
 
    # Konversi dari Celsius ke skala tujuan
    if skala_tujuan == "C":
        hasil = celsius
    elif skala_tujuan == "F":
        hasil = celsius * 9 / 5 + 32
    else:  # K
        hasil = celsius + 273.15
 
    return hasil
 
 
print("=== Konversi Suhu ===")
 
while True:
    suhu_input = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if suhu_input.lower() == "selesai":
        break
 
    skala_asal = input("Skala asal (C/F/K): ")
    skala_tujuan = input("Skala tujuan (C/F/K): ")
 
    try:
        suhu = float(suhu_input)
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal.upper()} = {hasil} {skala_tujuan.upper()}")
    except ValueError as e:
        print(f"Error: {e}")
 