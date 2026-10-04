class SkalaTidakDikenaliError(Exception):
    """Error khusus untuk skala suhu selain C, F, K."""
    pass

def konversi_suhu(suhu, skala_asal, skala_tujuan):
    """Mengonversi suhu antar skala C, F, K. Raise error jika skala tidak dikenal."""
    skala_valid = ("C", "F", "K")
    if skala_asal not in skala_valid or skala_tujuan not in skala_valid:
        raise SkalaTidakDikenaliError("Skala suhu tidak dikenali.")

    if skala_asal == "C":
        celsius = suhu
    elif skala_asal == "F":
        celsius = (suhu - 32) * 5 / 9
    else:  
        celsius = suhu - 273.15

    if skala_tujuan == "C":
        hasil = celsius
    elif skala_tujuan == "F":
        hasil = celsius * 9 / 5 + 32
    else:  
        hasil = celsius + 273.15

    return round(hasil, 2)

def main():
    print("=== Konversi Suhu ===")

    while True:
        masukan_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ").strip()
        if masukan_suhu.lower() == "selesai":
            break

        skala_asal = input("Skala asal (C/F/K): ").strip().upper()
        skala_tujuan = input("Skala tujuan (C/F/K): ").strip().upper()

        try:
            suhu = float(masukan_suhu)
            hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
            print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")
        except SkalaTidakDikenaliError as error:
            print(f"Error: {error}")
        except ValueError:
            print("Error: Suhu harus berupa angka.")

main()