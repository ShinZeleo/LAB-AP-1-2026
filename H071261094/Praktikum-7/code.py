with open("isi.txt", "r") as file:
    data = file.readlines()
    jumlah = 0
    for line in data:
        word = line.split()
        jumlah +=1
    print(f"Jumlah orang: {jumlah}")