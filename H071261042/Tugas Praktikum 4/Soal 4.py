#Processing input (Input dan konversi suhu)
def konversi_suhu(suhu, skala_asal, skala_tujuan):
    if skala_asal not in ("C", "F", "K") or skala_tujuan not in ("C", "F", "K"):
        raise ValueError("Skala suhu tidak dikenali.")
    #Konversi ke celcius
    if skala_asal == "C":
        celsius = suhu
    elif skala_asal == "F":
        celsius = (suhu - 32) * 5 / 9 #Rumus fahrenheit ke celcius
    else:
        celsius = suhu - 273.15 #Rumus kelvin ke celcius
    #Konversi celcius ke skala tujuan
    if skala_tujuan == "C":
        return celsius
    elif skala_tujuan == "F":
        return celsius * 9 / 5 + 32 #Rumus celcius ke fahrenheit
    else:
        return celsius + 273.15 #Rumus celcius ke kelvin

#Processing program
def main():
    print("=== Konversi Suhu ===")
    while True:
        masukan = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
        if masukan.strip().lower() == "selesai":
            break #Menghentikan proses input

        skala_asal = input("Skala asal (C/F/K): ").strip().upper()
        skala_tujuan = input("Skala tujuan (C/F/K): ").strip().upper()
        try:
            suhu = float(masukan)
            hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
            print(f"Hasil: {suhu} {skala_asal} = {round(hasil, 2)} {skala_tujuan}")
        except ValueError as e:
            if "Skala" in str(e):
                print(f"Error: {e}")
            else:
                print("Error: Suhu harus berupa angka.")

main()