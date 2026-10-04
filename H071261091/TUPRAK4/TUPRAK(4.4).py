def konversi_suhu (suhu = float, asal = str, tujuan = str) -> float:

    skala_valid = ["C","F","K"]

    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Error: Skala suhu tidak dikenali.")

    if asal == "C":
        suhu_celcius = suhu
    elif asal == "F":
        suhu_celcius = (suhu-32)*5/9
    elif asal == "K":
        suhu_celcius = suhu - 273.15

    if tujuan == "C":
        return suhu_celcius
    elif tujuan == "F":
        return (suhu_celcius * 9 / 5) + 32
    elif tujuan == "K":
        return suhu_celcius + 273.15


while True:
    print ("=== Konversi Suhu ===")
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if input_suhu.lower() == 'selesai':
        break

    skala_asal = input("Skala asal (C/F/K): ").upper()
    skala_tujuan = input("Skala tujuan (C/F/K): ").upper()

    try:
        suhu_valid = float(input_suhu)
        hasil = konversi_suhu (suhu_valid, skala_asal, skala_tujuan)
        print (f"Hasil Konversi; {suhu_valid} {skala_asal.upper()} = {hasil} {skala_tujuan.upper()}")

    except ValueError:
        print ("Error: Skala suhu tidak dikenali.")